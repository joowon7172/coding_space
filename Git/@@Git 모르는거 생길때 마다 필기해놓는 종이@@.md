# @@ Git 모르는거 생길 때 마다 필기해놓는 종이 @@



* #### main 브랜치에서 최초의 commit을 하지 않았을 때 나타나는 에러메시지

```
fatal: Not a valid object name: 'main'.
```

### 

* **브랜치 삭제**

```
git branch -d "브랜치명"
```



* **[ git add 취소 ]**

  - git reset (전체 파일 add 취소)

  - git reset HEAD 파일 (특정 파일 add 취소)

------

 

* **[ git commit 취소 ]**

  - git reset HEAD^ (가장 최신 커밋 1개 취소(삭제))

  - git reset HEAD^^(가장 최신 커밋 2개 취소(삭제))

  - 꺽쇠 갯수에 따라 최신 커밋을 필요한만큼 순서대로 삭제할 수 있음



* **.gitignore**

​	특정파일을 무시 후 커밋 가능



