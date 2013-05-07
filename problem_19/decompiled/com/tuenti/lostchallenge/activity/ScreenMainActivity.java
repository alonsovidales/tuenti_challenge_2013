package com.tuenti.lostchallenge.activity;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.text.Editable;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import com.tuenti.lostchallenge.service.SignalService;

public class ScreenMainActivity extends Activity
{
  private Button bt_start;
  private EditText et_channel;
  BroadcastReceiver signalReceiver = new BroadcastReceiver()
  {
    public void onReceive(Context paramAnonymousContext, Intent paramAnonymousIntent)
    {
      Log.d("service", "receiving :" + paramAnonymousIntent.getAction());
      if (paramAnonymousIntent.getAction().equals("com.tuenti.signal"))
        Toast.makeText(ScreenMainActivity.this, "THIS IS A SIGNAL", 1).show();
    }
  };

  private void hookListeners()
  {
    this.bt_start.setOnClickListener(new View.OnClickListener()
    {
      public void onClick(View paramAnonymousView)
      {
        try
        {
          if (SignalService.isConected)
          {
            SignalService.isConected = false;
            ScreenMainActivity.this.runOnUiThread(new Runnable()
            {
              public void run()
              {
                ScreenMainActivity.this.bt_start.setText(2130968581);
              }
            });
            return;
          }
          int i = Integer.parseInt(ScreenMainActivity.this.et_channel.getText().toString());
          if (i < 5)
          {
            ScreenMainActivity.this.runOnUiThread(new Runnable()
            {
              public void run()
              {
                ScreenMainActivity.this.bt_start.setText(2130968582);
              }
            });
            Intent localIntent = new Intent(ScreenMainActivity.this, SignalService.class);
            localIntent.putExtra("channel", i);
            ScreenMainActivity.this.startService(localIntent);
            return;
          }
        }
        catch (Exception localException)
        {
          Toast.makeText(ScreenMainActivity.this.getBaseContext(), "This is your channel, really?", 1).show();
          return;
        }
        Toast.makeText(ScreenMainActivity.this.getBaseContext(), "This is your channel, really?", 1).show();
      }
    });
  }

  private void mapUI()
  {
    this.et_channel = ((EditText)findViewById(2131165186));
    this.bt_start = ((Button)findViewById(2131165187));
    if (SignalService.isConected)
    {
      this.bt_start.setText(2130968582);
      return;
    }
    this.bt_start.setText(2130968581);
  }

  public void onCreate(Bundle paramBundle)
  {
    super.onCreate(paramBundle);
    setContentView(2130903040);
  }

  public boolean onCreateOptionsMenu(Menu paramMenu)
  {
    getMenuInflater().inflate(2131099648, paramMenu);
    return true;
  }

  protected void onDestroy()
  {
    super.onDestroy();
  }

  protected void onResume()
  {
    super.onResume();
    new IntentFilter("com.tuenti.signal");
    mapUI();
    hookListeners();
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.activity.ScreenMainActivity
 * JD-Core Version:    0.6.2
 */