class Solution {
    public String reverseVowels(String s) {
         int i = 0, j = s.length() - 1;
        char[] carr = s.toCharArray();
        while (i < j){
            if (!isVowel(carr[i])) i++;
            if (!isVowel(carr[j])) j--;

            if (isVowel(carr[i]) && isVowel(carr[j])){
                char temp = carr[i];
                carr[i++] = carr[j];
                carr[j--] = temp;
            }
        }
        return new String(carr);
    }

    private boolean isVowel(char c){
        switch (c){
            case 'A':
            case 'a':
            case 'E':
            case 'e':
            case 'I':
            case 'i':
            case 'O':
            case 'o':
            case 'U': 
            case 'u': return true;
            default: return false;
        }
    }
}