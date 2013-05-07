package datanative.tuenti.lostchallenge;

public class DataNative
{
  static
  {
    System.loadLibrary("keys");
  }

  public native String getKey(int paramInt);

  public native String[] getKeys();

  public native String[] getValues();
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     datanative.tuenti.lostchallenge.DataNative
 * JD-Core Version:    0.6.2
 */