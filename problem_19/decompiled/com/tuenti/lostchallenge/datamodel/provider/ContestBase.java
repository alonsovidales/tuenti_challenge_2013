package com.tuenti.lostchallenge.datamodel.provider;

import android.net.Uri;
import android.provider.BaseColumns;

public final class ContestBase
  implements BaseColumns
{
  public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.jwei512.contest";
  public static final Uri CONTENT_URI = Uri.parse("content://com.tuenti.lostchallenge.datamodel.provider.ContestProvider/contest");
  public static final String CONTEST_ID = "_id";
  public static final String KEY = "key";
  public static final String VALUE = "value";
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.datamodel.provider.ContestBase
 * JD-Core Version:    0.6.2
 */