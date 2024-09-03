class Solution {
    public int getLucky(String s, int k) {
        StringBuilder number = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int digit = ch - 'a' + 1;
            number.append(digit);
        }
        while (k > 0) {
            int sum = 0;
            for (int i = 0; i < number.length(); i++) {
                sum += number.charAt(i) - '0';
            }
            number = new StringBuilder();
            while (sum > 0) {
                number.append(sum % 10);
                sum /= 10;
            }
            k--;
        }
        return Integer.parseInt(number.reverse().toString());
    }
}
