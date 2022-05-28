def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    
    
    # ここから記述
    
    
    #基準値未満のグループと基準値以上のグループを分ける境界を求める関数(前半グループの末項のindexを返す)
    def border(array,i,j):
    # 配列の先頭を基準値とする 
        pivot=array[i]
        
        while (True):
            while(array[i]<pivot):
                i+=1
            while(array[j]>pivot):
                j-=1
    
            #i<jならばarray[i]とarray[j]を入れ替えi+1,j-1
            if i<j:
                array[i], array[j] = array[j], array[i]
                i+=1
                j-=1
                
            #i>=jとなったら停止 
            else:
                break
                
        return j
    
        
        
            
    #再帰を用いる
    #quicksort関数(配列名，配列の左端,配列の右端)
    def quicksort(array,l,r):
        if l<r:
            b=border(array,l,r)
            quicksort(array,l,b)
            quicksort(array,b+1,r)
    
    
        
    #初期条件
    #L:配列の左端のindex,R:右端のindex
    L=0
    R=len(array)-1
    

    quicksort(array,L,R)
    
    return array

    # ここまで記述
    

if __name__ == '__main__':
    main()
