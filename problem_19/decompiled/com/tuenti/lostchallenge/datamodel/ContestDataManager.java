package com.tuenti.lostchallenge.datamodel;

import android.content.ContentResolver;
import android.content.ContentValues;
import android.net.Uri;
import android.util.Log;
import com.tuenti.lostchallenge.datamodel.provider.ContestBase;
import com.tuenti.lostchallenge.encript.SimpleCrypto;
import datanative.tuenti.lostchallenge.DataNative;

public class ContestDataManager
{
  private static final String LOGTAG = "ContestDataManager";
  private static ContestDataManager instance = new ContestDataManager();
  private ContentResolver mContent;
  private boolean mInit = false;

  public static void Init(ContentResolver paramContentResolver)
  {
    if (!instance.mInit)
    {
      instance.mContent = paramContentResolver;
      instance.populateAllData();
      instance.mInit = true;
    }
  }

  private void addRow(ContestValue paramContestValue)
  {
    ContentValues localContentValues = new ContentValues();
    localContentValues.put("key", paramContestValue.getKey());
    localContentValues.put("value", paramContestValue.getValue());
    ContentResolver localContentResolver = this.mContent;
    Uri localUri = ContestBase.CONTENT_URI;
    String[] arrayOfString = new String[1];
    arrayOfString[0] = String.valueOf(paramContestValue.getKey());
    if (localContentResolver.update(localUri, localContentValues, "key=?", arrayOfString) == 0)
      this.mContent.insert(ContestBase.CONTENT_URI, localContentValues);
  }

  public static boolean isInit()
  {
    return instance.mInit;
  }

  private void populateAllData()
  {
    try
    {
      DataNative localDataNative = new DataNative();
      String[] arrayOfString1 = localDataNative.getKeys();
      String[] arrayOfString2 = localDataNative.getValues();
      SimpleCrypto localSimpleCrypto = new SimpleCrypto("test");
      for (int i = 0; ; i++)
      {
        if (i >= arrayOfString1.length)
          return;
        ContestValue localContestValue = new ContestValue();
        localContestValue.setKey(localSimpleCrypto.encrypt(arrayOfString1[i]));
        localContestValue.setValue(localSimpleCrypto.encrypt(arrayOfString2[i]));
        addRow(localContestValue);
      }
    }
    catch (Exception localException)
    {
      Log.e("ContestDataManager", "error populating", localException);
    }
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.datamodel.ContestDataManager
 * JD-Core Version:    0.6.2
 */