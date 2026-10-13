# Dell XPS 13 9350 · macOS Monterey

面向 **i5-6200U / HD 520 / 3200×1800 触摸屏 / DW1820A** 的 OpenCore 配置及排障记录。测试系统为 macOS **12.7.6 (21H1320)**，OpenCore **1.0.9**。

这是从实机可用 U 盘引导整理的脱敏基线，**保留跑码、使用内置文字启动菜单**。不是面向所有 9350 配置的一键通用包。最后实机验证日期：2026-10-12；发布整理日期：2026-10-13。本次发布未重新执行整机安装或完整硬件回归。

> **首次使用必须填写自己的 SMBIOS 身份信息。** 包内序列号、MLB、UUID 为空，ROM 为全零。不要直接拿空白配置登录 Apple 服务，也不要复制他人的序列号。系统恢复镜像不包含在仓库中。

## 硬件与验证状态

| 项目 | 状态与边界 |
|---|---|
| CPU / 内存 | Intel i5-6200U，8GB LPDDR3；CPU XCPM 已加载 |
| HD 520 核显 | 1536MB，Metal 支持；曾通过计算测试；内屏正常显示 |
| 内屏 | 3200×1800，系统显示缩放已验证为看起来像 1600×900；缩放偏好不随 EFI 分发 |
| 触摸屏 | 实机反馈可用；USB ELAN 触摸设备 |
| 触控板 | 已用于日常操作；全部手势、长时间稳定性未逐项验证 |
| Wi-Fi | DW1820A / BCM4350，PCI 14e4:43a3；扫描、关联无线网络和无线 SSH 已验证 |
| 蓝牙 | USB 0a5c:6412；固件加载、开启与外设使用有实机记录；睡眠唤醒时曾发生 bluetoothd 崩溃并恢复，重连稳定性仍需观察 |
| 普通睡眠 | 禁用深度休眠后，软件睡眠及合盖/开盖恢复已验证；长时间、电池耗尽场景未验证 |
| 深度休眠 | **未修复、未验证，不启用**；HibernationFixup 实验已撤销 |
| 声音、摄像头、读卡器、雷电、外接显示 | 配置中可能包含相关驱动，但没有完整专项验收，不作可用承诺 |
| USB | 局部映射及蓝牙端口已验证；USB-C、扩展坞等所有组合尚未完整验证 |

## 使用方法

1. 从 [Releases](https://github.com/zry116131/Dell-XPS13-9350-Hackintosh-Monterey/releases) 下载发布包并核对 `SHA256SUMS.txt`，或克隆仓库。
2. 用 [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) 等工具为 **MacBookPro13,1** 生成自己的序列号、MLB、UUID，设置自己的 6 字节 ROM。填写 `EFI/OC/config.plist → PlatformInfo → Generic`。详见 [身份信息说明](docs/IDENTITY.md)。
3. 执行 `python3 scripts/validate.py --require-identity` 检查必要字段及文件引用，再使用 **OpenCore 1.0.9 自带的 ocvalidate** 检查配置。
4. 备份原 EFI，将本包的 **EFI 文件夹**复制到测试 U 盘的 FAT32 启动分区根目录。先按 F12 选 UEFI USB 启动验证；不要直接覆盖唯一可用的硬盘 EFI。
5. macOS 安装/恢复镜像请从 Apple 官方渠道自行获取，可参考 [Dortania 恢复盘说明](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/)。仓库不包含 macOS 镜像或 Apple 账号。
6. 安装后阅读 [睡眠设置](docs/SLEEP.md)，执行 `bash scripts/set-shallow-sleep.sh`。这会修改系统电源设置，**仅复制 EFI 不会自动应用这些设置**。
7. 确认桌面、核显、输入、Wi-Fi、蓝牙及重启可用后，再自行备份并迁入内置盘 EFI。识别分区应使用 `diskutil list`，不要照抄他人的 disk 编号。固件启动路径为 `\EFI\BOOT\BOOTx64.efi`。

## BIOS 要点

- 使用 UEFI 启动，SATA Operation 设为 **AHCI**；Secure Boot 关闭。
- Wireless Device Enable 中启用 WLAN、Bluetooth。
- 若无线被硬件开关强制关闭，可解除 Wireless Switch 对 WLAN 的控制；它与 Wireless Device Enable 的硬件启用开关不同。
- 本次实机曾因 BIOS 设置丢失导致硬盘模式变化、无法启动。遇到突然不能开机，先检查 AHCI 等设置，不要立即替换 EFI。
- 不建议为套用教程恢复 BIOS 默认值，也不要直接清空 NVRAM。

## 本机关键修复

详见 [配置说明](docs/CONFIGURATION.md)。重点包括 HD 520 的显存预留补丁、DW1820A 的 ASPM/兼容属性和延迟初始化、蓝牙内部 USB 端口及固件驱动。

## 启动主题与跑码

发布基线不启用 OpenCanopy，保留 `-v debug=0x100 keepsyms=1`。曾在主题/缩放/跑码改动后遇到启动停滞，单独关闭跑码也出现过异常；没有足够证据把主题定为唯一原因。后续“仅主题”的硬盘配置不作为本次可靠基线。

## 文件、来源和隐私

- `EFI/`：脱敏后的可用基线；无实验休眠插件、无主题资源。
- `scripts/`：配置检查与浅睡设置，不包含远程登录、磁盘格式化或 EFI 自动覆盖脚本。
- `docs/`：配置、已知限制、身份设置和组件版本。
- `licenses/`、[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)：上游授权与来源信息。
- [PRIVACY.md](PRIVACY.md)：脱敏范围。

各组件版权归对应作者。仓库是配置整合与实机经验记录，不宣称拥有第三方驱动版权。分发的二进制保留原内容；脱敏及移除未启用主题资源后的包通过静态校验，仍须在使用者自己的机器上验证。
