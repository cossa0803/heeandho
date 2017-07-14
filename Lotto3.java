package ex0714;

public class Lotto3 {
	
	public static void main(String[] args) {
		
		int numRange = 45;
		int lottoNums[] = new int[numRange];
		int temp = 0;
		
		for (int i = 0; i < lottoNums.length; i++) {
			lottoNums[i] = i + 1;
		}
		
		for (int i = 0; i < 6; i++) {
			
			int randomIndex = (int)(Math.random() * numRange);
			
			temp = lottoNums[numRange - 1];
			lottoNums[numRange - 1] = lottoNums[randomIndex];
			lottoNums[randomIndex] = temp;
			
			numRange--;
		}
		
		for (int i = 0; i < 6; i++) {
			System.out.print(lottoNums[numRange++] + " ");
		}

	}
}
