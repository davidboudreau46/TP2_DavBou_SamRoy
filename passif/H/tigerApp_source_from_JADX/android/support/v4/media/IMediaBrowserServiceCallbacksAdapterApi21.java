package android.support.v4.media;

import android.media.session.MediaSession.Token;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import java.lang.reflect.Method;

class IMediaBrowserServiceCallbacksAdapterApi21 {
    private Method mAsBinderMethod;
    Object mCallbackObject;
    private Method mOnConnectFailedMethod;
    private Method mOnConnectMethod;
    private Method mOnLoadChildrenMethod;

    static class Stub {
        static Method sAsInterfaceMethod;

        Stub() {
        }

        static {
            try {
                sAsInterfaceMethod = Class.forName("android.service.media.IMediaBrowserServiceCallbacks$Stub").getMethod("asInterface", new Class[]{IBinder.class});
            } catch (ReflectiveOperationException e) {
                e.printStackTrace();
            }
        }

        static Object asInterface(IBinder binder) {
            Object result = null;
            try {
                result = sAsInterfaceMethod.invoke(null, new Object[]{binder});
            } catch (ReflectiveOperationException e) {
                e.printStackTrace();
            }
            return result;
        }
    }

    IMediaBrowserServiceCallbacksAdapterApi21(Object callbackObject) {
        this.mCallbackObject = callbackObject;
        try {
            Class theClass = Class.forName("android.service.media.IMediaBrowserServiceCallbacks");
            Class parceledListSliceClass = Class.forName("android.content.pm.ParceledListSlice");
            this.mAsBinderMethod = theClass.getMethod("asBinder", new Class[0]);
            this.mOnConnectMethod = theClass.getMethod("onConnect", new Class[]{String.class, Token.class, Bundle.class});
            this.mOnConnectFailedMethod = theClass.getMethod("onConnectFailed", new Class[0]);
            this.mOnLoadChildrenMethod = theClass.getMethod("onLoadChildren", new Class[]{String.class, parceledListSliceClass});
        } catch (ReflectiveOperationException e) {
            e.printStackTrace();
        }
    }

    IBinder asBinder() {
        IBinder result = null;
        try {
            return (IBinder) this.mAsBinderMethod.invoke(this.mCallbackObject, new Object[0]);
        } catch (ReflectiveOperationException e) {
            e.printStackTrace();
            return result;
        }
    }

    void onConnect(String root, Object session, Bundle extras) throws RemoteException {
        try {
            this.mOnConnectMethod.invoke(this.mCallbackObject, new Object[]{root, session, extras});
        } catch (ReflectiveOperationException e) {
            e.printStackTrace();
        }
    }

    void onConnectFailed() throws RemoteException {
        try {
            this.mOnConnectFailedMethod.invoke(this.mCallbackObject, new Object[0]);
        } catch (ReflectiveOperationException e) {
            e.printStackTrace();
        }
    }

    void onLoadChildren(String mediaId, Object parceledListSliceObj) throws RemoteException {
        try {
            this.mOnLoadChildrenMethod.invoke(this.mCallbackObject, new Object[]{mediaId, parceledListSliceObj});
        } catch (ReflectiveOperationException e) {
            e.printStackTrace();
        }
    }
}
