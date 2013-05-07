package com.tuenti.lostchallenge.datamodel.provider;

import android.content.ContentProvider;
import android.content.ContentResolver;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.content.UriMatcher;
import android.database.Cursor;
import android.database.MatrixCursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteQueryBuilder;
import android.net.Uri;
import android.util.Log;
import com.tuenti.lostchallenge.encript.SimpleCrypto;
import java.util.HashMap;

public class ContestProvider extends ContentProvider
{
  public static final String AUTHORITY = "com.tuenti.lostchallenge.datamodel.provider.ContestProvider";
  private static final int CONTEST = 1;
  private static final String CONTEST_TABLE_NAME = "contest";
  private static final String DATABASE_NAME = "contest.db";
  private static final int DATABASE_VERSION = 1;
  private static final String PRIVATEKEY = "test";
  private static final String TAG = "ContestProvider";
  private static HashMap<String, String> filmProjectionMap;
  private static final UriMatcher sUriMatcher = new UriMatcher(-1);
  private DatabaseHelper dbHelper;

  static
  {
    sUriMatcher.addURI("com.tuenti.lostchallenge.datamodel.provider.ContestProvider", "contest", 1);
    filmProjectionMap = new HashMap();
    filmProjectionMap.put("_id", "_id");
    filmProjectionMap.put("key", "key");
    filmProjectionMap.put("value", "value");
  }

  public int delete(Uri paramUri, String paramString, String[] paramArrayOfString)
  {
    SQLiteDatabase localSQLiteDatabase = this.dbHelper.getWritableDatabase();
    switch (sUriMatcher.match(paramUri))
    {
    default:
      throw new IllegalArgumentException("Unknown URI " + paramUri);
    case 1:
    }
    int i = localSQLiteDatabase.delete("contest", paramString, paramArrayOfString);
    getContext().getContentResolver().notifyChange(paramUri, null);
    return i;
  }

  public String getType(Uri paramUri)
  {
    switch (sUriMatcher.match(paramUri))
    {
    default:
      throw new IllegalArgumentException("Unknown URI " + paramUri);
    case 1:
    }
    return "vnd.android.cursor.dir/vnd.jwei512.contest";
  }

  public Uri insert(Uri paramUri, ContentValues paramContentValues)
  {
    if (sUriMatcher.match(paramUri) != 1)
      throw new IllegalArgumentException("Unknown URI " + paramUri);
    if (paramContentValues != null);
    for (ContentValues localContentValues = new ContentValues(paramContentValues); ; localContentValues = new ContentValues())
    {
      long l = this.dbHelper.getWritableDatabase().insert("contest", "key", localContentValues);
      if (l <= 0L)
        break;
      Uri localUri = ContentUris.withAppendedId(ContestBase.CONTENT_URI, l);
      getContext().getContentResolver().notifyChange(localUri, null);
      return localUri;
    }
    throw new SQLException("Failed to insert row into " + paramUri);
  }

  public boolean onCreate()
  {
    this.dbHelper = new DatabaseHelper(getContext());
    return true;
  }

  public Cursor query(Uri paramUri, String[] paramArrayOfString1, String paramString1, String[] paramArrayOfString2, String paramString2)
  {
    ((String[])null);
    if (paramArrayOfString2 == null);
    String[] arrayOfString1;
    int i;
    SQLiteQueryBuilder localSQLiteQueryBuilder;
    try
    {
      arrayOfString1 = new String[0];
      break label417;
      while (true)
      {
        int j = arrayOfString1.length;
        if (i >= j)
        {
          if ((paramString1 != null) && ((paramString1 == null) || (paramString1.contains("key"))))
            break;
          String[] arrayOfString2 = { "value" };
          String[] arrayOfString3 = { "I need the key sorry guy" };
          MatrixCursor localMatrixCursor1 = new MatrixCursor(arrayOfString2);
          localMatrixCursor1.addRow(arrayOfString3);
          return localMatrixCursor1;
          arrayOfString1 = new String[paramArrayOfString2.length];
          break label417;
        }
        SimpleCrypto localSimpleCrypto1 = new SimpleCrypto("test");
        arrayOfString1[i] = localSimpleCrypto1.encrypt(paramArrayOfString2[i]);
        i++;
      }
      localSQLiteQueryBuilder = new SQLiteQueryBuilder();
      switch (sUriMatcher.match(paramUri))
      {
      default:
        throw new IllegalArgumentException("Unknown URI " + paramUri);
      case 1:
      }
    }
    catch (Exception localException)
    {
      Log.e("error", "problem in query", localException);
      throw new IllegalArgumentException("Unknown error " + paramUri);
    }
    localSQLiteQueryBuilder.setTables("contest");
    localSQLiteQueryBuilder.setProjectionMap(filmProjectionMap);
    Cursor localCursor = localSQLiteQueryBuilder.query(this.dbHelper.getReadableDatabase(), paramArrayOfString1, paramString1, arrayOfString1, null, null, paramString2);
    String[] arrayOfString4 = localCursor.getColumnNames();
    int k = localCursor.getColumnCount();
    MatrixCursor localMatrixCursor2 = new MatrixCursor(arrayOfString4);
    label304: String[] arrayOfString5;
    if (localCursor.moveToFirst())
      arrayOfString5 = new String[k];
    for (int m = 0; ; m++)
    {
      if (m >= k)
      {
        localMatrixCursor2.addRow(arrayOfString5);
        if (localCursor.moveToNext())
          break label304;
        localMatrixCursor2.setNotificationUri(getContext().getContentResolver(), paramUri);
        return localMatrixCursor2;
      }
      if (localCursor.getType(m) == 3)
      {
        SimpleCrypto localSimpleCrypto2 = new SimpleCrypto("test");
        arrayOfString5[m] = localSimpleCrypto2.decrypt(localCursor.getString(m));
      }
      else
      {
        arrayOfString5[m] = localCursor.getString(m);
        continue;
        label417: i = 0;
        break;
      }
    }
  }

  public int update(Uri paramUri, ContentValues paramContentValues, String paramString, String[] paramArrayOfString)
  {
    SQLiteDatabase localSQLiteDatabase = this.dbHelper.getWritableDatabase();
    switch (sUriMatcher.match(paramUri))
    {
    default:
      throw new IllegalArgumentException("Unknown URI " + paramUri);
    case 1:
    }
    int i = localSQLiteDatabase.update("contest", paramContentValues, paramString, paramArrayOfString);
    getContext().getContentResolver().notifyChange(paramUri, null);
    return i;
  }

  private static class DatabaseHelper extends SQLiteOpenHelper
  {
    DatabaseHelper(Context paramContext)
    {
      super("contest.db", null, 1);
    }

    public void onCreate(SQLiteDatabase paramSQLiteDatabase)
    {
      paramSQLiteDatabase.execSQL("CREATE TABLE contest (_id INTEGER PRIMARY KEY AUTOINCREMENT,key TEXT,value TEXT);");
    }

    public void onUpgrade(SQLiteDatabase paramSQLiteDatabase, int paramInt1, int paramInt2)
    {
      Log.w("ContestProvider", "Upgrading database from version " + paramInt1 + " to " + paramInt2 + ", which will destroy all old data");
      paramSQLiteDatabase.execSQL("DROP TABLE IF EXISTS contest");
      onCreate(paramSQLiteDatabase);
    }
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.datamodel.provider.ContestProvider
 * JD-Core Version:    0.6.2
 */
