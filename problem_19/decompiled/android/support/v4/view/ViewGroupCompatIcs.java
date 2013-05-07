package android.support.v4.view;

import android.view.View;
import android.view.ViewGroup;
import android.view.accessibility.AccessibilityEvent;

class ViewGroupCompatIcs
{
  public static boolean onRequestSendAccessibilityEvent(ViewGroup paramViewGroup, View paramView, AccessibilityEvent paramAccessibilityEvent)
  {
    return paramViewGroup.onRequestSendAccessibilityEvent(paramView, paramAccessibilityEvent);
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     android.support.v4.view.ViewGroupCompatIcs
 * JD-Core Version:    0.6.2
 */