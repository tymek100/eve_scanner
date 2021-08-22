## Deployment to APK (on Debian linux)
1. Install buildozer and required linux packages.
```
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python3 setup.py install
sudo apt install cython
sudo apt install default-jdk
sudo apt install android-sdk
sudo apt install libffi-dev
sudo apt install libssl-dev
sudo apt install zip
unzip ~/.buildozer/android/platform/android-sdk/commandlinetools-linux-6514223_latest.zip
```
2. Initialize buildozer (inside eve_scanner directory).
```
buildozer init
```
3. Export debug APK.
```
buildozer -v android debug
```
