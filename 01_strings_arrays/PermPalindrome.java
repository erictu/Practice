import java.util.HashMap;

public class PermPalindrome {
  public static void main(String[] args) {
    System.out.println(palindrome(args[0]));
  }

  public static boolean palindrome(String input) {
    String replaced = input.replaceAll("\\s+",""); 
    char[] stringArr = replaced.toCharArray();
    HashMap<Character, Integer> mapped = new HashMap<Character, Integer>();
    for (char letter: stringArr) {
      System.out.println(letter);
      if (mapped.containsKey(letter)){
        // System.out.println("already contains");
        mapped.put(letter, mapped.get(letter)+1);
      } else {
        // System.out.println("putting for first time");
        mapped.put(letter, 1);
      }
    }
    boolean flag = false;
    for (char key: mapped.keySet()) {
      if (flag == true) {
        return false;
      }
      if (mapped.get(key)%2 == 1) {
        // System.out.println(key);
        // System.out.println(mapped.get(key));
        flag = true;
      }
    }
    return true;
  }
}