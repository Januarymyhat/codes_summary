class Solution {
    public int[][] generateMatrix(int n) {
        int startX = 0, startY = 0;
        int i, j;
        int offset = 1;
        int count = 1;
        int[][] result = new int[n][n];
        int loop = 1; // 记录当前的圈数

        // 一圈两行，一共 n 行，一共 n/2 圈
        while(loop <= n/2){
            for(j = startY; j<n-offset; j++){
                result[startX][j] = count++;
            }
            for(i = startX; i<n-offset; i++){
                result[i][j] = count++;
            }
            for(;j>startY; j--){
                result[i][j] = count++;
            }
            for(;i>startX; i--){
                result[i][j] = count++;
            }

            startX++;
            startY++;
            offset++;
            loop++;
        }

        if (n % 2 == 1) { // n 为奇数时，单独处理矩阵中心的值
            result[startX][startY] = count;
        }
        return result;

    }
}
