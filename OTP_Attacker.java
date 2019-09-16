package Vuln;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;

public class Vuln
{
	private static HttpsURLConnection con = null;
	static ByteBuffer buf  = null;
	static byte[] ba = null;

	
	public static int sub_routine(int idx,int r6)
	{
		 int limi = 4;
	     if (idx >= limi)
	     {
	    	 int result = 0;
	         result = buf.getInt(0);
	         result = result & 2147483647;
	         result = result % 100000000;
	         return result;
	     }
	     int r2 = idx + r6;
	     r2 = ba[r2];
	     buf.put(idx, (byte) r2);
		 return 0;
	}
	
	public static int generateOneTimePassword(javax.crypto.SecretKey r4, long r5)
	{
        Mac r0 = null;
		try {
			r0 = javax.crypto.Mac.getInstance("HmacSHA1");
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        try {
			r0.init(r4);
		} catch (InvalidKeyException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        buf = ByteBuffer.allocate(8);
        buf.putLong(0, r5);
        ba = buf.array();
        ba = r0.doFinal(ba);
        int r6 = ba.length - 1;
        r6 = ba[r6];
        r6 = r6 & 15;
        int idx = 0;
        int result = 0;
        while(true) {
        	result = sub_routine(idx,r6);
        	if(result != 0)
        		break;
        	idx += 1;
        }
        return result;
	}
	
	public static int query(int count_r5) throws IOException
	{
		// TODO Auto-generated method stub
		
		String SecretKey = "1234567890";
		int generate_key = generateOneTimePassword(new SecretKeySpec(SecretKey.getBytes(), 0, SecretKey.getBytes().length, "HmacSHA1"), count_r5);
		return  generate_key;
	}
	
	public static void copy(InputStream input, OutputStream output) throws IOException
	{
	    byte[] buffer = new byte[1024];
	    int n = 0;
	    while ((n = input.read(buffer)) != -1)
	    {
	        output.write(buffer, 0, n);
	    }
	}
		
	
	private static void printStream(Process process) throws IOException, InterruptedException 
	{
		process.waitFor();
    	try (InputStream psout = process.getInputStream())
    	{
        	copy(psout, System.out);
    	}
	}


	public static void byRuntime(String[] command) throws IOException, InterruptedException
	{
		Runtime runtime = Runtime.getRuntime();
		Process process = runtime.exec(command);
		printStream(process);
	}
	
	public static void main(String[] args) throws IOException, InterruptedException
	{
		for(int i = 306; i < 400; i++)
		{
			System.out.printf("[!] Index : %d\n", i);
			System.out.printf("[!] OTP Password : %s\n", query(i));
			String a[] = {"cmd","/c","python","C:\\Users\\DONGHYUN\\Desktop\\vuln.py", String.valueOf(query(i))};
			byRuntime(a);
		}
	}
	
