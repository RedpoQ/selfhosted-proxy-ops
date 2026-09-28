# Network counters

Capture interface `rx_dropped`, `tx_dropped`, driver errors, `/proc/net/softnet_stat`, and UDP receive/send/buffer errors. Counters are cumulative unless proven otherwise.

A nonzero number is `OBSERVED`, not a diagnosis. To justify tuning, establish counter deltas over a defined interval, concurrent traffic, correlated application failure, and a plausible subsystem. Keep `TUNING_ACTION_REQUIRED=NOT_EVALUATED` during a correctness baseline.
