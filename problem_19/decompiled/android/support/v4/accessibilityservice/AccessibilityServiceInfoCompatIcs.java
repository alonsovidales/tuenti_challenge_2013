package android.support.v4.accessibilityservice;

import android.accessibilityservice.AccessibilityServiceInfo;
import android.content.pm.ResolveInfo;

class AccessibilityServiceInfoCompatIcs
{
  public static boolean getCanRetrieveWindowContent(AccessibilityServiceInfo paramAccessibilityServiceInfo)
  {
    return paramAccessibilityServiceInfo.getCanRetrieveWindowContent();
  }

  public static String getDescription(AccessibilityServiceInfo paramAccessibilityServiceInfo)
  {
    return paramAccessibilityServiceInfo.getDescription();
  }

  public static String getId(AccessibilityServiceInfo paramAccessibilityServiceInfo)
  {
    return paramAccessibilityServiceInfo.getId();
  }

  public static ResolveInfo getResolveInfo(AccessibilityServiceInfo paramAccessibilityServiceInfo)
  {
    return paramAccessibilityServiceInfo.getResolveInfo();
  }

  public static String getSettingsActivityName(AccessibilityServiceInfo paramAccessibilityServiceInfo)
  {
    return paramAccessibilityServiceInfo.getSettingsActivityName();
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     android.support.v4.accessibilityservice.AccessibilityServiceInfoCompatIcs
 * JD-Core Version:    0.6.2
 */