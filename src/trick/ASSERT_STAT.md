#### 파이썬 코드를 정돈하기 위한 패턴



##### `assert`문으로 방어하기

- 단언문 `assert`문이 뭐고, 왜 사용해야 하지?

  > 프로그램 안정성을 높이고 프로그램을 쉽게 디버그 할 수 있다. - 책 본문중

  - 단언문 예제

    ```python
    def apply_discount(product, discount):
        price = int(product['price'] * (1.0 - discount))
        assert 0 <= price <= product['price']
        return price
    ```

  > 계산된 할인 가격은 `0` 보다 작을수 없고, 할인 가격은 실제 물건 가격보다 클 수 없다.
  >
  > assert를 활용하여 실제로 의도한 대로 작동하는지 확인한다.
  >
  > assert를 사용하는 가장 큰 이유는 문제가 생겼을때 프로그램을 쉽게 디버깅 할 수 있다는 것이다.



- 그냥 일반적인 예외 처리를 사용하면 안되나?

  > 단언문을 사용한다는 것은 예상할 수 있는 예외를 처리하고자 함이 아니다.
  >
  >  `File-Not-Found` 같이 파일을 찾지 못하면, 사용자가 적절히 예외를 처리하듯 예상되는 예외를 
  >
  > 처리하고자 단언문을 사용하는 것이 아니라, 진짜 프로그램에 에러가 있는지 확인하고,
  >
  > 에러 발생시 디버깅이 수월하게 하는 목적으로 사용한다.
  >
  > 단언문은 런타임 에러를 처리하기 위한 메커니즘이 아니라 디버깅을 돕는 것임을 명심하자.(책 본문중)



- assert를 사용하면 안되는 경우

  - 데이터 검증용으로 사용하면 안됨

    > 파이썬 설정으로 assert를 무력화 할 수 있음. 
    > 만약 들어온 유저가 관리자인지 판단하는 코드를 assert로 만들고 해당 설정이 꺼져있다면
    >
    > 어떤 유저든지 관리자 권한으로 접근하게 되는 우를 범할 수 있음.
    
    ```python
    def delete_product(prod_id, user):
        assert user.is_admin(), 'Must be admin'
        assert store.has_product(prod_id), 'Unknown product'
        store.get_product(prod_id).delete()
    ```
    
  - 절대 실패하지 않는 단언문
  
    > 항상 `참`이 되는 파이썬 단언문을 실수로 작성할 수 있다.
    > assert 문에서 첫 번째 인자로 `튜플`을 전달하면 그 단언문은 항상 참이 된다.
  
    ```python
    assert (1 == 2, 'This should fail')
    ```
  
    > lint에서 어느 정도 방어를 해주지만,  단언문 선언 후 해당 단언문이 반드시 실패되는지
    >
    > 테스트 해야 한다.

