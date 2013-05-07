package android.support.v4.view;

import android.animation.ValueAnimator;
import android.graphics.Paint;
import android.view.View;

class ViewCompatHC
{
  static long getFrameTime()
  {
    return ValueAnimator.getFrameDelay();
  }

  public static int getLayerType(View paramView)
  {
    return paramView.getLayerType();
  }

  public static void setLayerType(View paramView, int paramInt, Paint paramPaint)
  {
    paramView.setLayerType(paramInt, paramPaint);
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     android.support.v4.view.ViewCompatHC
 * JD-Core Version:    0.6.2
 */