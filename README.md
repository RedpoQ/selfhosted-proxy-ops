# 自建代理运维指南（Self-Hosted Proxy Ops）

[English](README.en.md)

一套面向中文用户的、**证据驱动**的自建代理运维 Skills：从选 VPS 地区、检查服务器、3X-UI/Xray、协议测试、客户端接入，一直到最终验收和“停止继续折腾”。

它不是一键安装脚本，也不承诺“某个地区一定最好”“某个协议一定最快”。核心目标是：**先确定问题在哪一层，再只改必要的那一层，并且每次修改都有证据和回滚路径。**

## 这个项目解决什么问题

自建代理经常会出现一种情况：

- 面板里看起来配置正确；
- 配置文件里也写对了；
- 但生成配置、运行状态、订阅内容或真实流量其实并不一致。

这个项目把这些层明确分开：

```text
声明配置
    ↓
生成配置
    ↓
运行时状态
    ↓
真实流量
```

越靠后的证据越可靠。**“文件里写了”不等于“运行时已经生效”。**

如果你只是想了解某个协议是什么，不需要从整个生命周期开始；如果你正在搭建、排障、比较线路或准备上线，则建议从 `proxy-stack-lifecycle` 开始。

## 先从这里开始

告诉 Agent：

> 请使用 `proxy-stack-lifecycle`，先检查我的客户端、当前网络、VPS、代理客户端、域名、Cloudflare、是否有第二台设备，以及 Agent 是否依赖当前代理。先只读检查，不要直接修改生产环境。

然后按它给出的下一步进入对应 Skill。

核心流程只有 8 步：

1. **能力与安全检查**：先确认你有什么设备、权限、网络和回滚条件。
2. **VPS 地区/线路适配**：判断当前用户网络到 VPS 的真实路径是否合适。
3. **VPS 基础正确性**：检查 DNS、路由、时间、资源、包管理等基础问题。
4. **控制面 / 数据面**：当前 v0.1 已实现 3X-UI + Xray 适配。
5. **最小可用代理**：先建立一个确定能工作的 baseline。
6. **客户端接入**：处理 TUN、DNS、规则、生成配置和运行时。
7. **端到端验收**：从客户端一路验证到最终出口。
8. **Freeze**：已经通过验收后，没有新证据就停止继续调参。

详细流程见 [生命周期](docs/lifecycle.md) 和 [架构说明](docs/architecture.md)。

## 8 个 Skills 是做什么的

| Skill | 中文职责 | 什么时候用 |
|---|---|---|
| `proxy-stack-lifecycle` | 总入口 / 阶段判断 | 不知道问题在哪一层，或者准备从头搭建 |
| `vps-region-fit` | VPS 地区与线路适配 | 比较 San Jose、Tokyo、LA 等地区，判断当前 ISP 到哪个区域更合适 |
| `vps-baseline` | VPS 基础健康检查 | DNS、路由、时间、系统资源、包管理异常 |
| `xui-xray-stack` | 3X-UI + Xray 治理 | 面板、域名、TLS、Cloudflare、Xray runtime、订阅不一致 |
| `proxy-transport-lab` | 协议与线路实验 | 比较 Reality / Hysteria2 / TUIC / XHTTP，或测试优选 Edge |
| `special-egress-routing` | 特殊出口路由 | 只有某类流量需要静态/住宅/二级 SOCKS 出口 |
| `proxy-client-governance` | 客户端治理 | Clash/Mihomo 的 TUN、DNS、规则、代理组、本地路由问题 |
| `proxy-stack-acceptance` | 最终验收与冻结 | 系统已经能用，判断是否真的应该停止继续优化 |

### 容易混淆的边界

- **选 VPS 地区** → `vps-region-fit`
- **比较已经存在的协议** → `proxy-transport-lab`
- **Cloudflare 架构/域名/TLS** → `xui-xray-stack`
- **Cloudflare 默认 Edge vs 优选 IP 性能** → `proxy-transport-lab`
- **客户端规则/TUN/DNS** → `proxy-client-governance`
- **服务端特殊出口隔离** → `special-egress-routing`

## Shadow Test：只有一台电脑也能安全测试

默认测试思路不是直接改正在使用的 Clash，而是建立一条旁路测试路径：

```text
生产路径
→ 保持不动

Shadow 测试路径
→ 独立进程
→ 独立临时配置
→ 独立 localhost 高位端口
→ TUN 关闭
→ System Proxy 关闭
→ 只有显式测试请求经过它
```

这样可以在同一台机器上比较新协议或新线路，而不必先破坏当前可用网络。

Shadow 只能隔离应用层测试，它**不能替代**真正的生产 TUN、系统 DNS 和 OS 路由验收。因此流程是：

```text
Shadow PASS
→ 小范围 Production Smoke Test
→ 最终验收
```

## 可选能力，不是必做步骤

以下功能只有在你的环境确实需要时才启用：

- 域名 / DNS / TLS
- Cloudflare Edge
- Cloudflare 优选 IP
- 多协议 benchmark
- 特殊静态/住宅出口
- 订阅投影
- Shadow Test
- 可回滚的单变量性能实验

项目不会因为“网上都这么配”就默认打开它们。

一个组件如果移除后所有验收条件仍然通过，就优先保留更简单的系统。

## 支持情况

| 范围 | 当前状态 |
|---|---|
| Windows 客户端治理 | `ENV_SPECIFIC_REFERENCE` |
| Linux VPS 基线 | `ENV_SPECIFIC_REFERENCE` |
| 3X-UI + Xray | `ENV_SPECIFIC_REFERENCE` |
| Mihomo Shadow Test 模式 | `ENV_SPECIFIC_REFERENCE` |
| Linux 客户端 | `PARTIAL_REFERENCE` |
| macOS | `UNVERIFIED` |
| OpenWrt | `UNVERIFIED_OPTIONAL` |

`ENV_SPECIFIC_REFERENCE` 表示：这些工作流来自真实环境并经过核对，但**不代表对所有地区、ISP、版本和机器都完成了普遍验证**。

`PARTIAL_REFERENCE` 表示只有部分路径有实际证据。

`UNVERIFIED` / `UNVERIFIED_OPTIONAL` 不应被描述成“已经生产验证”。

更多证据等级见 [证据清单说明](docs/evidence-inventory.md)。

## v0.1 明确不做什么

- 不提供通用“一键生产自动化框架”。
- 不宣称支持所有控制面；当前实现适配器是 **3X-UI + Xray**。
- `vps-baseline` 不负责“无脑优化 VPS”。
- `proxy-transport-lab` 只允许**隔离、单变量、可测量、可回滚**的实验性调优。
- 不默认要求 24 小时压力测试；只有出现间歇性故障、高方差或候选难分时才升级测试等级。
- 不把功能可用等同于安全加固完成。

## 安全与回滚

默认动作等级是：

```text
READ_ONLY
```

只有证据和条件满足后才升级到：

```text
CONTROLLED_MUTATION
EXPERIMENTAL_SHADOW
PRODUCTION_CHANGE
```

任何生产修改都应满足：

```text
基线
→ 备份
→ 回滚路径
→ 一次只改一个主要变量
→ 静态验证
→ 应用
→ Runtime 验证
→ 真实流量验证
```

如果 Agent 自己依赖正在修改的代理，回滚机制必须**不依赖 Agent 继续在线**。

## Secret 处理

不要向公开仓库提交：

- VPS 真实 IP
- 真实域名和面板隐藏路径
- SSH 密码 / 私钥
- UUID
- Reality / HY2 / TUIC 凭据
- 订阅 URL / token
- Cloudflare API token
- 静态出口账号、密码或真实出口 IP

公开示例使用 `example.com`、RFC 5737 TEST-NET 和 `<REDACTED_...>` 占位符。

详细规则见 [Secret Handling](docs/methodology/secret-handling.md)。

## 项目状态

当前是 **v0.1 release candidate**，仓库已经公开。

已完成：

- 8 个 Skills 静态校验
- 相对链接检查
- Secret 静态扫描
- Skill 边界与冲突案例
- 合成测试 fixtures
- 仓库级静态检查器

仍属于已知验证缺口：

- portable plugin 安装烟测
- 真正的模型 Skill activation eval
- 更广泛的 macOS / OpenWrt / 多 ISP 实机验收

因此本项目目前的定位仍然是：**knowledge + workflow first**，不是生产自动部署器。

## License

MIT，见 [LICENSE](LICENSE)。
