@echo off
setlocal

REM Set download URLs
set SDK_URL=https://dl.google.com/android/repository/commandlinetools-win-8512546_latest.zip
set NDK_URL=https://dl.google.com/android/repository/android-ndk-r21e-windows-x86_64.zip

REM Set installation paths
set INSTALL_PATH=C:\Android
set SDK_PATH=%INSTALL_PATH%\cmdline-tools
set NDK_PATH=%INSTALL_PATH%\ndk

REM Create installation directories
mkdir %SDK_PATH%
mkdir %NDK_PATH%

REM Download and extract Android SDK command line tools
echo Downloading Android SDK command line tools...
curl -o %SDK_PATH%\cmdline-tools.zip %SDK_URL%
echo Extracting Android SDK command line tools...
powershell -Command "Expand-Archive -Path '%SDK_PATH%\cmdline-tools.zip' -DestinationPath '%SDK_PATH%'"
del %SDK_PATH%\cmdline-tools.zip

REM Download and extract Android NDK
echo Downloading Android NDK...
curl -o %NDK_PATH%\ndk.zip %NDK_URL%
echo Extracting Android NDK...
powershell -Command "Expand-Archive -Path '%NDK_PATH%\ndk.zip' -DestinationPath '%NDK_PATH%'"
del %NDK_PATH%\ndk.zip

REM Set environment variables
setx ANDROID_SDK_ROOT "%SDK_PATH%"
setx ANDROID_NDK_ROOT "%NDK_PATH%\android-ndk-r21e"
setx Path "%Path%;%SDK_PATH%\bin;%SDK_PATH%\tools;%SDK_PATH%\tools\bin;%NDK_PATH%\android-ndk-r21e"

REM Verify installations
echo Verifying installations...
java -version
sdkmanager --list
ndk-build --version

echo Installation complete. Please restart your command prompt or PowerShell to apply changes.

endlocal
pause
