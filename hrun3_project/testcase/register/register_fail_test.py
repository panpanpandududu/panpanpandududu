# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\register\register_fail.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseRegisterFail(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user-psw-email": [
                    ["", "123456", "123@qq.com"],
                    ["a", "123456xx", "123@qq.com"],
                    ["aaaaaaaaaabbbbbbbbbbcccccccccc12", "", "123@qq.com"],
                    ["testx123", "", "123@qq.com"],
                    ["testx123", "12345", "123@qq.com"],
                    ["testx123", "12345678912345678", "123@qq.com"],
                    ["testx123", "123456", "12345"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("注册用例-注册失败场景").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("注册失败-参数不合法")
            .post("/api/v1/register")
            .with_json({"username": "$user", "password": "$psw", "email": "$email"})
            .validate()
            .assert_equal("body.code", 3003)
            .assert_equal("body.msg", "参数不合法")
        ),
    ]


if __name__ == "__main__":
    TestCaseRegisterFail().test_start()
