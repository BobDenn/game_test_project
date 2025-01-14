# 项目启动步骤

## 1. 环境准备
1. 启动 MuMu 模拟器
2. 确保游戏已安装
3. 检查设备连接：
   ```bash
   adb devices
   ```
   如果没有设备显示，运行：
   ```bash
   adb connect 127.0.0.1:16384
   ```

## 2. 启动 Appium 服务器
打开命令窗口，运行：
```bash
appium --base-path /wd/hub --log-level error --relaxed-security
```
等待服务器启动完成。

## 3. 运行测试
打开新的命令窗口：
```bash
cd D:\game_test_project
python -m unittest test_cases.test_environment -v
```

## 常见问题解决
1. 如果 adb devices 没有显示设备：
   - 检查模拟器是否完全启动
   - 重新运行 adb connect 命令

2. 如果 Appium 启动失败：
   - 检查端口 4723 是否被占用
   - 重启 Appium 服务器

3. 如果测试运行失败：
   - 检查模拟器和游戏是否正常运行
   - 检查 config.yaml 中的配置是否正确 