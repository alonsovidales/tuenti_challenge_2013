package com.tuenti.lostchallenge.service;

import android.app.Service;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Bitmap.CompressFormat;
import android.graphics.Bitmap.Config;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Paint.Style;
import android.graphics.Rect;
import android.os.Handler;
import android.os.IBinder;
import android.util.Log;
import com.tuenti.lostchallenge.datamodel.ContestDataManager;
import datanative.tuenti.lostchallenge.DataNative;
import java.io.ByteArrayOutputStream;

public class SignalService extends Service
{
  public static final String ACTION_SEND_DATA = "com.tuenti.signal";
  public static final String CHANNEL = "channel";
  private static final String DATA_INFO = "SIGNAL_INFO";
  private static final int NUM_PARTS = 5;
  private static final long TIME_INTERVAL_SIGNAL = 5000L;
  public static boolean isConected = false;
  private Handler handler;
  private byte[] imageArray = null;
  private int position = 0;
  Runnable sender = new Runnable()
  {
    public void run()
    {
      SignalService.this.sendData();
      if (SignalService.isConected)
        SignalService.this.handler.postDelayed(SignalService.this.sender, 5000L);
    }
  };

  private String convertString()
  {
    StringBuffer localStringBuffer = new StringBuffer();
    for (int i = 0; ; i++)
    {
      if (i >= this.imageArray.length)
        return localStringBuffer.toString();
      localStringBuffer.append((char)this.imageArray[i]);
    }
  }

  private void initDataImage(String paramString)
  {
    Bitmap localBitmap1 = BitmapFactory.decodeResource(getResources(), 2130837506);
    Bitmap localBitmap2 = Bitmap.createBitmap(localBitmap1.getWidth(), localBitmap1.getHeight(), Bitmap.Config.ARGB_4444);
    Canvas localCanvas = new Canvas(localBitmap2);
    localCanvas.drawBitmap(localBitmap1, 0.0F, 0.0F, null);
    Paint localPaint = new Paint();
    localPaint.setColor(-16777216);
    localPaint.setStyle(Paint.Style.FILL);
    Rect localRect = new Rect();
    localPaint.setTextSize(200.0F);
    localPaint.getTextBounds(paramString, 0, paramString.length(), localRect);
    localCanvas.drawRect(new Rect(0, -15 + localBitmap1.getHeight() - localRect.height(), localBitmap1.getWidth(), -10 + localBitmap1.getHeight()), localPaint);
    localPaint.setColor(-1);
    localCanvas.drawText(paramString, (localBitmap1.getWidth() - localRect.width()) / 2, -15 + localBitmap1.getHeight(), localPaint);
    ByteArrayOutputStream localByteArrayOutputStream = new ByteArrayOutputStream();
    localBitmap2.compress(Bitmap.CompressFormat.JPEG, 85, localByteArrayOutputStream);
    this.imageArray = localByteArrayOutputStream.toByteArray();
  }

  private void sendData()
  {
    Intent localIntent = new Intent();
    localIntent.setAction("com.tuenti.signal");
    if (this.position < 4);
    for (byte[] arrayOfByte = new byte[this.imageArray.length / 5]; ; arrayOfByte = new byte[this.imageArray.length - this.position * (this.imageArray.length / 5)])
    {
      System.arraycopy(this.imageArray, this.position * (this.imageArray.length / 5), arrayOfByte, 0, arrayOfByte.length);
      localIntent.putExtra("SIGNAL_INFO", arrayOfByte);
      Log.d("service", "sending broadcast");
      sendBroadcast(localIntent);
      this.position = ((1 + this.position) % 5);
      return;
    }
  }

  public IBinder onBind(Intent paramIntent)
  {
    throw new UnsupportedOperationException("Not bind");
  }

  public void onCreate()
  {
    super.onCreate();
    this.handler = new Handler();
  }

  public int onStartCommand(Intent paramIntent, int paramInt1, int paramInt2)
  {
    Log.d("service", "start service");
    int i = paramIntent.getIntExtra("channel", -1);
    if (i != -1)
    {
      String str = new DataNative().getKey(i);
      Log.d("borrar", "from native " + str);
      initDataImage(str);
      ContestDataManager.Init(getContentResolver());
      isConected = true;
    }
    sendData();
    this.handler.postDelayed(this.sender, 5000L);
    return super.onStartCommand(paramIntent, paramInt1, paramInt2);
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.service.SignalService
 * JD-Core Version:    0.6.2
 */
