package android.support.v4.net;

import android.net.TrafficStats;
import java.net.Socket;
import java.net.SocketException;

public class TrafficStatsCompatIcs
{
  public static void clearThreadStatsTag()
  {
    TrafficStats.clearThreadStatsTag();
  }

  public static int getThreadStatsTag()
  {
    return TrafficStats.getThreadStatsTag();
  }

  public static void incrementOperationCount(int paramInt)
  {
    TrafficStats.incrementOperationCount(paramInt);
  }

  public static void incrementOperationCount(int paramInt1, int paramInt2)
  {
    TrafficStats.incrementOperationCount(paramInt1, paramInt2);
  }

  public static void setThreadStatsTag(int paramInt)
  {
    TrafficStats.setThreadStatsTag(paramInt);
  }

  public static void tagSocket(Socket paramSocket)
    throws SocketException
  {
    TrafficStats.tagSocket(paramSocket);
  }

  public static void untagSocket(Socket paramSocket)
    throws SocketException
  {
    TrafficStats.untagSocket(paramSocket);
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     android.support.v4.net.TrafficStatsCompatIcs
 * JD-Core Version:    0.6.2
 */