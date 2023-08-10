package BOJ

fun main() {
    var n = readLine()!!.toInt()
    var turn = -1
    while (n>0){
        if (n>=3){
            n-=3
            turn *= -1
        }else{
            n-=1
            turn *= -1
        }
    }

    if (turn == 1){
        println("SK")
    }else{
        println("CY")
    }
}