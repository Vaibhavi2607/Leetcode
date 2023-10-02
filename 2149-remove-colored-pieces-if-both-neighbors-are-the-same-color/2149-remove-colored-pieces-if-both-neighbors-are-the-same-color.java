class Solution {
    public boolean winnerOfGame(String colors) {
        int n=colors.length();
        if(n<=2) return false;
        int alice=0,bob=0;
        for(int i=2;i<n;i++){
            char ch1=colors.charAt(i-2);
            char ch2=colors.charAt(i-1);
            char ch3=colors.charAt(i);
            if(ch1=='A'&&ch2=='A'&&ch3=='A') alice++;
            if(ch1=='B'&&ch2=='B'&&ch3=='B') bob++;
        }
        if(alice>bob) return true;
        return false;
    }
}