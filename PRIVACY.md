# 脱敏说明

发布包使用独立目录重新构建，不包含原工作目录的 Git 历史。

- 清空 SMBIOS 序列号、主板序列号（MLB）、SystemUUID；ROM 置为 6 字节零。
- 不包含 Apple 账号、Wi-Fi SSID/密码、蓝牙外设名称、局域网地址、真实网卡地址、设备 Service Tag。
- 不包含 SSH 密钥/授权文件、sudoers、远程调试脚本、原始诊断日志、硬件报告、照片、磁盘镜像或 NVRAM 转储。
- 移除 .DS_Store、AppleDouble 元数据；发布 ZIP 不携带扩展属性。
- 保留公开硬件标识、PCI 路径、ACPI 内容、SMBIOS 模型及驱动版权信息，这些是复用配置所需的数据。
- 上游二进制可能带有其作者的编译路径或版权姓名，不能将其视为本机用户数据。

使用者填写私人身份后，请勿将修改后的 config.plist 公开提交。

Sequoia 发布另移除了本机 `bluetoothInternalControllerInfo`、`bluetoothExternalDongleFailed` NVRAM 缓存及 EFI 内历史配置备份；不对第三方二进制做内容重写。
