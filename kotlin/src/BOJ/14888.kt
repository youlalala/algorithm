package BOJ

fun main(){

    val n = readln().toInt()
    val nums = readln().split(" ").map { it.toInt() }
    val symbolsCnt = readln().split(" ").map { it.toInt() }.toMutableList()

    var maxResult = (-1e9).toInt()
    var minResult = 1e9.toInt()

    fun dfs(idx: Int, result: Int){
        if (idx == n){
            if (maxResult < result){
                maxResult = result
            }
            if (minResult > result){
                minResult = result
            }
            return
        }
        for (i in 0 until 4){
            if(symbolsCnt[i] > 0){
                symbolsCnt[i]-=1
                when(i){
                    0 -> {
                        dfs(idx+1, result + nums[idx])
                    }1 -> {
                        dfs(idx+1, result - nums[idx])
                    }2 -> {
                        dfs(idx+1, result * nums[idx])
                    }3 -> {
                        dfs(idx+1, result / nums[idx])
                    }
                }
                symbolsCnt[i]+=1
            }
        }
    }

    dfs(1,nums[0])
    println(maxResult)
    println(minResult)

}

