package com.tuenti.lostchallenge.encript;

import android.util.Base64;
import java.io.IOException;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;

public class SimpleCrypto
{
  Cipher dcipher;
  Cipher ecipher;

  public SimpleCrypto(String paramString)
  {
    byte[] arrayOfByte = { -87, -101, -56, 50, 86, 52, -29, 3 };
    try
    {
      PBEKeySpec localPBEKeySpec = new PBEKeySpec(paramString.toCharArray(), arrayOfByte, 19);
      SecretKey localSecretKey = SecretKeyFactory.getInstance("PBEWithMD5AndDES").generateSecret(localPBEKeySpec);
      this.ecipher = Cipher.getInstance(localSecretKey.getAlgorithm());
      this.dcipher = Cipher.getInstance(localSecretKey.getAlgorithm());
      PBEParameterSpec localPBEParameterSpec = new PBEParameterSpec(arrayOfByte, 19);
      this.ecipher.init(1, localSecretKey, localPBEParameterSpec);
      this.dcipher.init(2, localSecretKey, localPBEParameterSpec);
      return;
    }
    catch (InvalidAlgorithmParameterException localInvalidAlgorithmParameterException)
    {
      System.out.println("EXCEPTION: InvalidAlgorithmParameterException");
      return;
    }
    catch (InvalidKeySpecException localInvalidKeySpecException)
    {
      System.out.println("EXCEPTION: InvalidKeySpecException");
      return;
    }
    catch (NoSuchPaddingException localNoSuchPaddingException)
    {
      System.out.println("EXCEPTION: NoSuchPaddingException");
      return;
    }
    catch (NoSuchAlgorithmException localNoSuchAlgorithmException)
    {
      System.out.println("EXCEPTION: NoSuchAlgorithmException");
      return;
    }
    catch (InvalidKeyException localInvalidKeyException)
    {
      System.out.println("EXCEPTION: InvalidKeyException");
    }
  }

  public String decrypt(String paramString)
  {
    try
    {
      byte[] arrayOfByte = Base64.decode(paramString, 0);
      String str = new String(this.dcipher.doFinal(arrayOfByte), "UTF8");
      return str;
    }
    catch (IOException localIOException)
    {
      return null;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      break label32;
    }
    catch (IllegalBlockSizeException localIllegalBlockSizeException)
    {
      break label32;
    }
    catch (BadPaddingException localBadPaddingException)
    {
      label32: break label32;
    }
  }

  public String encrypt(String paramString)
  {
    try
    {
      byte[] arrayOfByte = paramString.getBytes("UTF8");
      String str = new String(Base64.encode(this.ecipher.doFinal(arrayOfByte), 0));
      return str;
    }
    catch (IOException localIOException)
    {
      return null;
    }
    catch (UnsupportedEncodingException localUnsupportedEncodingException)
    {
      break label35;
    }
    catch (IllegalBlockSizeException localIllegalBlockSizeException)
    {
      break label35;
    }
    catch (BadPaddingException localBadPaddingException)
    {
      label35: break label35;
    }
  }
}

/* Location:           /Volumes/socialpoint/tuenti_challenge_3/problem_19/jar/
 * Qualified Name:     com.tuenti.lostchallenge.encript.SimpleCrypto
 * JD-Core Version:    0.6.2
 */
