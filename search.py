def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number =7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    #初期条件
    #R:配列の右端のindex,L:配列の左端のindex
    R=len(sorted_array)-1
    L=0
    
    
    
    while (R-L)>=0:
        mid=(R+L)//2
        
        #中間値と対象番号が一致したらその中間値のindexを返す
        if sorted_array[mid]==target_number:
            return mid
        
        #対象番号が中間値より大きい場合，左端を中間から一つ右のindexに変更
        if sorted_array[mid]<target_number:
            L=mid+1

     
        #対象番号が中間値より小さい場合，右端を中間から一つ左のindexに変更
        else:
            R=mid-1

       

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
