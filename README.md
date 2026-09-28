# VPS 自建代理运维指南

`vps-proxy-ops` · VPS Proxy Ops

[English](README.en.md)

一套面向中文用户的 VPS 自建代理运维工作流与 Agent Skills（智能体技能），判断以实际运行证据为准。

面板显示正常，不代表配置生成正确；生成配置写对了，不代表运行时已经加载生效；运行时显示在线，真实流量依然可能在客户端规则、DNS 或运营商线路上出问题。

本项目按照下面的证据层级判断问题：

```text
Declared configuration（面板填写配置）
↓
Generated configuration（落盘生成配置）
↓
Runtime state（进程运行时状态）
↓
Observed traffic（观测到的真实流量）
```

验收时优先采用更靠近运行结果的证据。真实流量最有参考价值，但测量前仍要检查 TUN、VPN、系统代理、ProxyCommand 等是否污染了测试路径。

先确认问题出在哪一层，再改哪一层。改动前留下基线与备份，改动后保留回滚路径。

---

## 适合谁，不适合谁

**适合这样的场景：**

- 买了第一台 VPS，不知道该从哪里下手排查。
- 节点突然连不上，搞不清是 VPS 路由、面板、Xray，还是客户端规则出了问题。
- 正在使用 Windows，或部分验证过的 Linux 客户端，搭配 3X-UI + Xray 与 Clash Verge / Mihomo。
- 想测试 Reality、Hysteria2、TUIC、XHTTP 等传输方式，但不想碰坏正在用的生产节点。
- 需要接入 Cloudflare、处理 TLS 证书、配置静态或住宅出口，或者调整 TUN 与 Fake-IP。
- 让 AI Agent 协助排障，但要求 Agent 按顺序找证据，不能盲目修改生产环境。

**本项目不包含以下内容：**

- **不把一键脚本作为主要交付方式**：不同环境之间差异很大，直接跳过中间状态会增加排障难度。
- **不分享免费节点**：不收集、不分发任何代理节点。
- **不推荐 VPS 厂商**：VPS 表现取决于本地 ISP、机房网络、运营商互联和实际路由，按实测结果选地区与线路。
- **不做协议排行榜**：某次测试中的协议赢家不会被推广成所有地区、运营商和时间段的结论。
- **不把功能可用等同于安全加固完成**：`FUNCTIONAL_READY` 与 `SECURITY_HARDENED` 分开判断。

---

## 快速指引

如果你不知道问题在哪一层，先调用 `proxy-stack-lifecycle`。

它会检查当前阶段，核对手里可用的资源（VPS、域名、Cloudflare、客户端），并确认执行排查的 Agent 是否依赖当前代理，避免改挂代理后把自己一起断开。这个 Skill 只做梳理与引导，不改生产配置。

如果问题已经很明确，直接对照下表：

| 遇到这类情况 | 先用这个 Skill | 它做什么 |
| :--- | :--- | :--- |
| 刚拿到 VPS，不知道选哪个机房，或者连上去很慢 | `vps-region-fit` | 测量 RTT、抖动、丢包、TCP/TLS、UDP 可达性和路径污染，用数据比较线路 |
| SSH 能连，但系统时钟、DNS 或基础网络行为异常 | `vps-baseline` | 检查 Linux VPS 正确性，确认 resolver ownership、网卡与路由状态，不做无证据调优 |
| 面板显示正常，但订阅拉出来的节点连不上 | `xui-xray-stack` | 梳理 3X-UI、持久化 DB、模板、Xray runtime 与订阅投影之间的断点 |
| 想尝试新协议，担心把现有可用节点搞崩 | `proxy-transport-lab` | 使用 Shadow Test 隔离测试，单变量对比，确认可用后再做少量生产 smoke test |
| 某些网站需要固定 IP 或住宅代理分流 | `special-egress-routing` | 配置专用出口，同时反向验证普通流量没有误走特殊出口 |
| 节点连通，但浏览器打不开网页，或 TUN 抓不到流量 | `proxy-client-governance` | 治理 Clash Verge / Mihomo，理清 TUN、Fake-IP 与分流规则 |
| 以为修好了，想确认整条链路到底能不能交付 | `proxy-stack-acceptance` | 执行端到端验收；阻塞性验收项通过后，决定是否进入 `FREEZE` |

---

## 8 阶段运维生命周期

整个代理栈按顺序推进。前置阶段没跑通时，先别急着跳到后面调参。

```text
1. 能力与安全条件发现 (Capability & Safety Discovery)
   ↓
2. 线路与地区适配 (VPS Region / Path Fit)
   ↓
3. VPS 基础正确性 (VPS Correctness Baseline)
   ↓
4. 控制面与数据面治理 (Control / Data Plane: 3X-UI + Xray)
   ↓
5. 建立最小可用代理 (Minimal Working Proxy)
   ↓
6. 客户端规则与分流接入 (Client Integration)
   ↓
7. 端到端验收 (End-to-End Acceptance)
   ↓
8. 固化，停止无意义调优 (Freeze)
```

1. **能力与安全条件发现**：识别当前网络环境、VPS 规格、域名解析权及客户端工具。判断当前排查会话是否借由该 VPS 代理通信，防止操作中途把自己踢下线。
2. **线路与地区适配**：拿本地真实 ISP 去测目标机房。地区好坏是测出来的，不是按地图距离猜出来的。
3. **VPS 基础正确性**：排查系统时钟、DNS Resolver 归属、默认路由、IPv4/IPv6、包管理和 failed systemd units。
4. **控制面与数据面**：从持久化 DB 与模板开始，核对控制面生成结果、Xray runtime 与订阅投影。
5. **建立最小可用代理**：先跑通最简单的一条基线节点。基础节点不通时，不要急着叠复杂反代或分流。
6. **客户端接入**：接入 Clash Verge / Mihomo，处理 TUN、DNS、Fake-IP 映射与规则组。
7. **端到端验收**：覆盖服务端基线、协议握手、订阅解析、客户端路由、出口是否符合预期、Fail-Closed 与回滚能力。
8. **固化**：阻塞性验收项通过，剩余缺口均为非阻塞项，且没有新的故障证据或业务需求时，进入 `FREEZE`。

---

## 8 个 Skills 说明

每个 Skill 对应项目中的独立目录，目录名保持原样不变。

### proxy-stack-lifecycle

项目总入口。负责判断当前链路所处阶段、用户手里有哪些资源、Agent 与代理之间的依赖关系，以及下一步应该进入哪个 Skill。它只做研判与调度，不直接修改生产环境。

### vps-region-fit

负责本地网络到 VPS 机房的实际链路测试。测量 RTT、Jitter（抖动）、丢包率、TCP/TLS、UDP 可达性，并检查 TUN、VPN、系统代理等是否污染测量路径。

原则很简单：**Region selection is measured, not guessed.**

### vps-baseline

负责 Linux VPS 的基础环境正确性排查。检查系统时间、DNS resolver ownership、路由表、IPv4/IPv6、包管理器、资源占用、失败服务和网卡计数器。

默认不做无证据的 sysctl 调优，不凭单个 counter 调 socket buffer，不盲猜 MTU，也不因为“大家都这么配”就强制切换 BBR。

### xui-xray-stack

当前 v0.1 实现的控制面适配器是 3X-UI + Xray。

它按照下面的 source-of-truth 关系排查：

```text
持久化 DB
→ Template
→ 控制面生成配置
→ Xray runtime
→ Subscription projection
```

覆盖域名角色、TLS/ACME、Cloudflare、Xray runtime 与订阅投影。不要只看一份 `config.json` 就判断 Xray 当前运行状态。

### proxy-transport-lab

负责受控实验，包括 Reality、Hysteria2、TUIC、XHTTP，以及 Cloudflare 默认 Edge 与 preferred edge 的对照。

测试遵循单变量原则。客户端优先使用独立 Shadow 进程、独立临时配置和 localhost 高位端口；服务端如需测试新协议，使用独立 candidate inbound/tag，不替换现有生产入口。

Shadow PASS 后，再用真实客户端做少量 production smoke test，并验证 TUN、DNS 和路由。

### special-egress-routing

负责特殊出口分流，适用于静态 IP、住宅 IP、二级 SOCKS5 或特定业务专属出口。

除了验证目标流量确实走了特殊出口，还要反向检查普通流量没有误走特殊出口。

### proxy-client-governance

负责客户端流量接管与规则治理。

Windows 侧已有较完整的 Clash Verge / Mihomo 参考流程；Linux 客户端目前只有部分路径经过验证。排查范围包括 TUN、DNS、Fake-IP、规则组、生成配置、运行时和最终流量。

### proxy-stack-acceptance

负责最终端到端验收。

检查服务端基线、线路质量、控制面一致性、传输握手、服务端路由、订阅格式、客户端解析、TUN、DNS、客户端分流、出口是否符合预期、Fail-Closed 与备份回滚能力。

阻塞性验收项通过，剩余问题都属于非阻塞缺口，而且没有新的故障证据或需求时，执行 `FREEZE=YES`。

---

## 几个常用方法

### Shadow Test（影子测试）

只有一台 VPS 和一台日常电脑时，也可以把测试路径和生产路径分开。

```text
生产路径
→ 保持现有入口不变

Shadow 测试路径
→ 独立进程
→ 独立临时配置
→ 独立 localhost 高位端口
→ TUN OFF
→ System Proxy OFF
→ 只有显式测试请求经过它
```

如果服务端需要新增候选协议，创建独立 candidate inbound/tag，不替换正在工作的入口。

客户端只让显式指定端口的测试请求进入 Shadow，例如：

```bash
curl -x socks5h://127.0.0.1:<TEST_PORT> https://example.com
```

Shadow Test 隔离的是应用层测试，不会模拟第二个 ISP 或第二条物理网络。Shadow PASS 后，再用真实客户端做 3 到 5 次 production smoke test，并检查 TUN、DNS 和路由。

### 一次只改一个变量

不要把换协议、改 DNS、换 TUN stack、调 MTU 和改分流规则堆在一次修改里。

一次只改一个主要变量。测完、对比、记录，再决定下一项。

### 消融（Ablation）

如果拿掉某个复杂配置层以后，端到端验收仍然通过，就保留更简单的结构。

这条规则适用于额外反代、复杂重写、全局脚本、特殊 DNS 层和其它可选组件。

### 复杂度预算（Complexity Budget）

Cloudflare、额外 DNS、特殊出口和自动化脚本都会增加故障面、维护成本和 ownership 复杂度。

如果一项改动既没有解决明确需求，也没有带来可验证收益，就不保留。

### 自适应测试（Adaptive Testing）

日常不用每次都挂 24 小时压测：

- **L0**：配置静态检查与语法解析。
- **L1**：3 到 5 次快速 smoke test。
- **L2**：采样 20 到 50 次，耗时约 5 到 15 分钟，作为日常默认级别。

只有 L2 出现间歇性失败、指标波动很大，或者两个候选难分时，才升级到 L3（30 到 60 分钟）或 L4（long soak）。

---

## 当前支持状态

| 模块 / 平台 | 支持状态 | 状态说明 |
| :--- | :--- | :--- |
| Windows 客户端治理（Clash Verge / Mihomo） | `ENV_SPECIFIC_REFERENCE` | 来自实际 Windows 环境核对，不能推论所有系统版本和网络环境完全相同 |
| Linux VPS 基础正确性检查 | `ENV_SPECIFIC_REFERENCE` | 来自特定真实 Linux VPS 环境，不能推论覆盖所有发行版、内核或虚拟化架构 |
| 3X-UI + Xray | `ENV_SPECIFIC_REFERENCE` | 来自真实环境核对；当前只实现这一控制面适配器 |
| Shadow Mihomo 测试模式 | `ENV_SPECIFIC_REFERENCE` | 已在现有环境验证基本模式；不同平台的进程、端口和路由行为仍需分别确认 |
| Linux 客户端 | `PARTIAL_REFERENCE` | 只有部分环境和路径有真实测试证据 |
| macOS | `UNVERIFIED` | 尚无完整端到端生产验证 |
| OpenWrt | `UNVERIFIED_OPTIONAL` | 当前没有标准化生产验证 |

- `ENV_SPECIFIC_REFERENCE`：有真实环境证据并经过核对，但属于特定环境样本，不代表适配所有机型、版本和 ISP。
- `PARTIAL_REFERENCE`：只有部分路径有真实证据，证据链还不完整。
- `UNVERIFIED / UNVERIFIED_OPTIONAL`：当前没有完整生产验收证据。

---

## 安全与敏感信息

提交 Issue、PR、日志或向 AI 发送排查上下文时，不要附带真实敏感凭据：

- VPS 真实公网 IP、真实解析域名
- 真实部署端口布局、非公开管理端口和面板隐藏路径
- SSH 用户名、密码、私钥
- UUID、Reality / TLS 等私密密钥材料
- Hysteria2 / TUIC 的密码和验证 secret
- 包含 token 的完整订阅地址
- Cloudflare API token / Global API Key
- 静态 / 住宅出口服务商的账号、密码和真实出口信息

公开示例使用：

- 域名：`example.com`
- IPv4：RFC 5737 TEST-NET，例如 `192.0.2.0/24`、`198.51.100.0/24`、`203.0.113.0/24`
- 文本占位符：`<REDACTED_IP>`、`<REDACTED_DOMAIN>`、`<REDACTED_SECRET>`

TEST-NET 只用于文档和 fixture。真实网络测量应使用你拥有、获授权或服务商明确提供的实际测试端点。

详细规则见 [Secret Handling](docs/methodology/secret-handling.md)。

---

## v0.1 当前边界与已知缺口

使用前先确认这些范围：

- **没有通用全自动一键部署框架**：v0.1 提供工作流、安全边界和回滚原则，不提供通用生产自动化。
- **控制面适配有限**：当前实现 3X-UI + Xray。其它控制面可以参考通用方法论，但仓库还没有对应适配器。
- **不做系统级 VPS 极限调优**：`vps-baseline` 只处理 correctness；实验性调优必须隔离、单变量、可测量、可回滚。
- **macOS 与 OpenWrt 尚未验证**：相关系统没有形成完整生产证据链。
- **验证工具链仍有缺口**：portable plugin install smoke、真正的模型 Skill activation eval，以及更广泛的多 ISP / 多平台实机验收尚未完成。

---

## 深入文档

- [系统架构概览](docs/architecture.md)
- [生命周期](docs/lifecycle.md)
- [证据等级与记录方式](docs/evidence-inventory.md)
- [证据层级](docs/methodology/evidence-hierarchy.md)
- [Shadow Test](skills/proxy-transport-lab/references/shadow-testing.md)
- [3X-UI / Xray Source of Truth](skills/xui-xray-stack/references/source-of-truth.md)
- [特殊出口与路由隔离](skills/special-egress-routing/references/route-isolation.md)

---

## 项目状态

当前为 **v0.1 release candidate**。

已完成：

- 8 个 Skills 静态校验
- 相对链接检查
- Secret 静态扫描
- Skill 边界与冲突案例
- 合成测试 fixtures
- 仓库级静态检查器

仍未完成：

- portable plugin 安装 smoke test
- 真正的模型 Skill activation eval
- 更广泛的 macOS / OpenWrt / 多 ISP 实机验收

项目当前以 **knowledge + workflow first** 为定位，不是生产自动部署器。

---

## License

[MIT](LICENSE)
