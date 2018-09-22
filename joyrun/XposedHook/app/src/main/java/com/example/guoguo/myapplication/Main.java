package com.example.guoguo.myapplication;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage;
import static de.robv.android.xposed.XposedHelpers.findAndHookMethod;
import de.robv.android.xposed.XC_MethodHook;


public class Main implements IXposedHookLoadPackage {
    public void handleLoadPackage(final XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        if (!lpparam.packageName.equals("co.runner.app"))
            return;
        XposedBridge.log("Loaded app:" + lpparam.packageName);
        findAndHookMethod("co.runner.app.jni.NativeToolImpl", lpparam.classLoader, "getSignatureV2", String.class,
                String.class, String.class, new XC_MethodHook() {

                    @Override
                    protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
                        XposedBridge.log("开始劫持了~");
                        XposedBridge.log("参数1 = " + param.args[0]);
                        XposedBridge.log("参数2 = " + param.args[1]);
                        XposedBridge.log("参数3 = " + param.args[2]);
                    }

                    @Override
                    protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                        XposedBridge.log("劫持结束了~");
                        XposedBridge.log("参数1 = " + param.args[0]);
                        XposedBridge.log("参数2 = " + param.args[1]);
                        XposedBridge.log("参数3 = " + param.args[2]);
                    }
                });
    }

}
