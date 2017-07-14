package array;

import java.util.Arrays;

public class Lotto1 {

	public static void main(String[] args) {

		int[] lottoNums = new int[6];

		outer: for (int i = 0; i < lottoNums.length; i++) {

			int randomNum = (int) (Math.random() * 45 + 1);

			for (int j = 0; j < i; j++) {
				if (randomNum == lottoNums[j]) {
					i--;
					System.out.println("중복나왔다");
					continue outer;
				}
			}
			lottoNums[i] = randomNum;
		}
		System.out.println(Arrays.toString(lottoNums));
	}
}
