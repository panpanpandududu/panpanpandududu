# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\sign\sign_login.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseSignLogin(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user-psw-code-msg-len_token": [
                    ["test", "123456", 0, "login success!", 40],
                    ["test_xxx_1", "123456", 3003, "账号或密码不正确", 0],
                    ["test1", "123456xx", 3003, "账号或密码不正确", 0],
                    ["", "", 3003, "账号或密码不正确", 0],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("登录sign签名接口")
        .variables(
            **{
                "user": "test",
                "psw": "123456",
                "code": 0,
                "msg": "login success!",
                "len_token": 40,
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("测试步骤：login")
            .setup_hook("${setup_request($request)}")
            .post("/api/v3/login")
            .with_json({"username": "$user", "password": "$psw", "sign": "x"})
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
            .assert_length_equal("body.token", "$len_token")
        ),
    ]


if __name__ == "__main__":
    TestCaseSignLogin().test_start()
