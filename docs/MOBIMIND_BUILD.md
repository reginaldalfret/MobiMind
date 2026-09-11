# MobiMind Build & Packaging Guide

## Prerequisites
- **Node.js:** v20+ or v22 LTS
- **Yarn:** 1.22.x
- **JDK:** OpenJDK 21 (configured as JAVA_HOME)
- **Android SDK & NDK:** NDK version 27.0.12077973 or 27.3.13750724

---

## Environment Setup
Set standard environment variables:
`ash
export JAVA_HOME=/path/to/jdk-21
export ANDROID_HOME=/path/to/android-sdk
export PATH=/bin:/platform-tools:/cmdline-tools/latest/bin:
`

---

## Compiling the Android APK

### Debug Build
`ash
cd android
./gradlew assembleProdDebug
`

The compiled APK will be generated at:
`	ext
android/app/build/outputs/apk/prod/debug/app-prod-debug.apk
`

### Release Build
`ash
cd android
./gradlew assembleProdRelease
`

---

## Deploying to Device or Waydroid

### Physical Android Device:
`ash
adb install -r android/app/build/outputs/apk/prod/debug/app-prod-debug.apk
`

### Waydroid Environment:
`ash
waydroid shell -- pm install -r /data/local/tmp/app-prod-debug.apk
`

---

## Verifying Model Installation
GGUF models can be pushed directly to app storage for offline use:
`ash
adb push ./models/q2-test/google_gemma-3-1b-it-Q2_K.gguf /data/user/0/com.pocketpalai/files/models/local/
`
