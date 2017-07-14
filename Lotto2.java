package array;

import java.util.Arrays;

public class Lotto2 {

	public static void main(String[] args) {

		int lottoNums[] = new int[45];
		int results[] = new int[6];

		for (int i = 0; i < lottoNums.length; i++) {
			lottoNums[i] = i + 1;
		}

		for (int i = 0; i < results.length; i++) {
			int idx = (int) (Math.random() * 45);

			if (lottoNums[idx] == -1) {
				i--;
				System.out.println("중복나왔다");
				continue;
			}
			results[i] = lottoNums[idx];
			lottoNums[idx] = -1;
		}

		System.out.println(Arrays.toString(results));
	}

}
