## 1. **merge**로 합치기

`add-coach` 브랜치를 `main` 브랜치로 **merge**

- `main` 브랜치로 이동
- 아래의 명령어로 병합

```
git merge add-coach
```

- 소스트리에서 확인

**이렇게 하면 main에서 추가한것과 add-coach에서 추가한것이 다 같이 나타남**



## 💡 `merge`는 `reset`으로 되돌리기 가능

- `merge`도 하나의 커밋
- `merge`하기 전 해당 브랜치의 마지막 시점으로



## 병합된 브랜치는 삭제

삭제 전 소스트리에서 `add-coach` 위치 확인

```
git branch -d add-coach
```



## 2. **rebase**로 합치기

`new-teams` 브랜치를 `main` 브랜치로 **rebase**

- `new-teams` 브랜치로 이동

  - 🛑 `merge`때와는 반대!

  

- 아래의 명령어로 병합

```
git rebase main
```



- 소스트리에서 상태 확인

  - **`main` 브랜치는 뒤쳐져 있는 상황!!!**

  

- `main` 브랜치로 이동 후 아래 명령어로 `new-teams`의 시점으로 **fast-forward**

  **헷갈리지만** **이 부분은 branch 심화 과정에서 다루게 됨**

```
git merge new-teams
```

이렇게 하면 main 브랜치가 new-teams 브랜치 위치로 옳겨지게 됨



- `new-teams` 브랜치 삭제



