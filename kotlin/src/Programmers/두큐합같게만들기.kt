// https://school.programmers.co.kr/learn/courses/30/lessons/118667

class Solution {
    fun solution(queue11: IntArray, queue22: IntArray): Int {
        var answer: Int = 0
        val max_cnt: Int = (queue11.size + queue22.size)*2

        var queue1 = ArrayDeque<Long>()
        var queue2 = ArrayDeque<Long>()
        for (i in queue11.indices) {
            queue1.add(queue11[i].toLong())
            queue2.add(queue22[i].toLong())
        }

        var sum1: Long = queue1.sum()
        var sum2: Long = queue2.sum()

        while(sum1 != sum2){
            if (sum1 >= sum2){
                var element = queue1.removeFirst()
                sum1 -= element
                sum2 += element
                queue2 += element
                answer += 1
            }else{
                var element = queue2.removeFirst()
                sum2 -= element
                sum1 += element
                queue1 += element
                answer += 1
            }
            if (answer > max_cnt){
                answer = -1
                break
            }
        }

        return answer
    }
}

fun main(){
    val solution = Solution()
    println(solution.solution(intArrayOf(3, 2, 7, 2), intArrayOf(4, 6, 5, 1)))
}