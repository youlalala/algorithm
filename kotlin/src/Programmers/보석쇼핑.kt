fun solution(gems: Array<String>): IntArray {
    var answer = intArrayOf()

    var typelist = gems.toSet()
    var min_term = gems.size

    var start:Int = 0
    var end:Int = 0

    var dict = HashMap<String,Int>()
    dict[gems[0]]=1

    while(start<=end){
        if(dict.count() == typelist.size){
            if(min_term > end-start){
                min_term = end-start
                answer = intArrayOf(start+1,end+1)

            }else{
                if(dict.containsKey(gems[start])) {
                    var num:Int = dict[gems[start]]!!
                    dict[gems[start]] =  num-1
                }
                if (dict[gems[start]] == 0){
                    dict.remove(gems[start])
                }
                start += 1
            }
        }else if(dict.count() < typelist.size){
            end += 1
            if(end == gems.size) {break}
            if(gems[end] in dict){
                if(dict.containsKey(gems[end])) {
                    var num:Int = dict[gems[end]]!!
                    dict[gems[end]] = num + 1
                }

            }else{
                dict[gems[end]]=1
            }
        }
    }
    return answer
}