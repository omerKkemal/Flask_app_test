[app]

# (str) Title of your application
title = MyFlaskApp

# (str) Package name
package.name = myflaskapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,flask,android,pyjnius,openssl

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (bool) Indicates if the application should be fullscreen or not
fullscreen = 1

# (bool) Allow background execution (for Android services)
android.allow_backup = true

# (bool) Enable WebView (for Android WebView)
android.webview = true

#
# OSX Specific
#

#
# author = © Copyright Info

# (str) App versioning (method 2)
# version = 1.0

# (str) SDL version to use
# sdl_version = 2.0.5

# (str) iOS deployment target
# ios.deployment_target = 9.0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (list) Features (adds uses-feature -tags to manifest)
#android.features = android.hardware.camera

# (int) Target Android API, should be as high as possible.
#android.api = 28

# (int) Minimum Android API version supported by your application
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 23

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use private storage (for Android)
#android.private_storage = true

# (bool) Uses the Androidx support library (for Android)
#android.x = false

# (bool) Expand the Android app to fill the entire screen (for Android)
#android.fullscreen = false

# (bool) Enable multi-dex support (for Android)
#android.multidex = false

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (str) The name of the Android app to build
#android.appname = MyFlaskApp

# (str) The path to the Android app to build
#android.app_path = 

# (str) The path to the Android app to build
#android.app_dir = 

# (str) The path to the Android app to build
#android.app_build_dir = 

# (str) The path to the Android app to build
#android.app_libs_dir = 

# (str) The path to the Android app to build
#android.app_src_dir = 

# (str) The path to the Android app to build
#android.app_res_dir = 

# (str) The path to the Android app to build
#android.app_assets_dir = 

# (str) The path to the Android app to build
#android.app_manifest = 

# (str) The path to the Android app to build
#android.app_java_dir = 

# (str) The path to the Android app to build
#android.app_native_lib_dir = 

# (str) The path to the Android app to build
#android.app_native_lib_import_dir = 

# (str) The path to the Android app to build
#android.app_native_lib_import_dir = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (str) Path to the buildozer data directory
# data_dir = .buildozer

# (str) Path to the buildozer data directory
# buildozer_data_dir = .buildozer

# (str) Path to the buildozer data directory
# buildozer_data_dir = .buildozer

# (str) Path to the buildozer data directory
# buildozer_data_dir = .buildozer

# (str) Path to the buildozer data directory
# buildozer_data_dir = .buildozer

# (str) Path to the buildozer data directory
# buildozer_data_dir = .buildozer

#-------------------------------------------------------------------------------
# [DEFAULT]
# 
# (str) Title of your application
# title = My Application
# 
# (str) Package name
# package.name = myapp
# 
# (str) Package domain (needed for android/ios packaging)
# package.domain = org.example
# 
# (str) Source code where the main.py live
# source.dir = .
# 
# (list) Source files to include (let empty to include all the files)
# source.include_exts = py,png,jpg,kv,atlas
# 
# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*.png
# 
# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec
# 
# (list) List of directory to exclude (let empty to not exclude anything)
# source.exclude_dirs = tests, bin
# 
# (list) List of exclusions using pattern matching
# source.exclude_patterns = license,images/*/*.jpg
# 
# (str) Application versioning (method 1)
# version = 1.0
# 
# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py
# 
# (list) Application requirements
# requirements = python3,kivy
# 
# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy
# 
# (list) Garden requirements
# garden_requirements =
# 
# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png
# 
# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png
# 
# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
# orientation = portrait
# 
# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY
# 
# (bool) Indicates if the application should be fullscreen or not
# fullscreen = 0
# 
# (bool) Allow background execution (for Android services)
# android.allow_backup = true
# 
# (bool) Enable WebView (for Android WebView)
# android.webview = true
# 
# (list) Permissions
# android.permissions = INTERNET
# 
# (int) Target Android API, should be as high as possible.
# android.api = 28
# 
# (int) Minimum Android API version supported by your application
# android.minapi = 21
# 
# (int) Android SDK version to use
# android.sdk = 23
# 
# (str) Android NDK version to use
# android.ndk = 19b
# 
# (bool) Use private storage (for Android)
# android.private_storage = true
# 
# (bool) Uses the Androidx support library (for Android)
# android.x = false
# 
# (bool) Expand the Android app to fill the entire screen (for Android)
# android.fullscreen = false
# 
# (bool) Enable multi-dex support (for Android)
# android.multidex = false
# 
# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a