# 普通睡眠与深度休眠

实机曾在合盖及自动睡眠后重启，诊断为 `Sleep Wake failure in EFI`，代码 `0x00000000 0x0000001f`。这一代码不能单独锁定具体驱动。

当前验证方案：

```sh
sudo pmset -a sleep 0 hibernatemode 0 standby 0 autopoweroff 0 powernap 0
```

- `hibernatemode 0`：普通内存睡眠，需要持续供电。
- `standby 0`、`autopoweroff 0`：不自动转换到深度休眠。
- `powernap 0`：关闭 Power Nap。
- `sleep 0`：关闭自动闲置睡眠；手动睡眠和合盖睡眠仍可触发。
- 显示器熄屏时间、开盖唤醒偏好保持原值。

可以用 `bash scripts/set-shallow-sleep.sh` 备份当前设置后应用上述方案。系统设置对所有启动盘共用，拔掉测试 U 盘不会撤销。

普通睡眠及合盖恢复有成功记录；不是深度休眠修复。睡眠仍消耗电量，长时间携带或闲置应关机。唤醒时出现过一次蓝牙服务崩溃并重新启动，不能宣称所有外设恢复完全稳定。

深度休眠实验使用过 HibernationFixup 和 HibernateMode=Auto，但用户停止了测试，没有确认恢复原会话。最终 EFI 没有包含该插件，HibernateMode=None。

参考：[Dortania Sleep](https://dortania.github.io/OpenCore-Post-Install/universal/sleep.html)、[HibernationFixup](https://github.com/acidanthera/HibernationFixup)。
