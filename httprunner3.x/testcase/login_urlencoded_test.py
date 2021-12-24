# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\login_urlencoded.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginUrlencoded(HttpRunner):

    config = Config("login-v4").base_url("http://49.235.92.12:8201")

    teststeps = [
        Step(
            RunRequest("step-login")
            .post("/api/v4/login")
            .with_data({"username": "test", "password": "123456"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "login success!")
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginUrlencoded().test_start()
