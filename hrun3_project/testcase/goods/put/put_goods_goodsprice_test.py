# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\goods\put\put_goods_goodsprice.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcase.login.login_success_test import TestCaseLoginSuccess as LoginSuccess


class TestCasePutGoodsGoodsprice(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "goodsname-goodscode-goodsprice-code-msg": [
                    ["yoyo123", "sp_test1", None, 0, "success!"],
                    ["yoyo123", "sp_test1", "", 3003, "参数不合法"],
                    ["yoyo123", "sp_test1", 19, 0, "success!"],
                    ["yoyo123", "sp_test1", 19.1, 0, "success!"],
                    ["yoyo123", "sp_test1", 19.1011, 0, "success!"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("更新商品信息")
        .variables(
            **{
                "sp_id": 1,
                "goodsname": "yoyo",
                "goodscode": "sp_test1",
                "merchantid": "10001",
                "merchantname": "悠悠学堂",
                "goodsprice": 99.9,
                "stock": 100,
                "goodsgroupid": 0,
                "goodsstatus": 1,
                "price": 21.0,
                "code": 0,
                "msg": "success!",
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(RunTestCase("step1-login").call(LoginSuccess).export(*["token"])),
        Step(
            RunRequest("更新商品信息")
            .put("/api/v2/goods/$sp_id")
            .with_headers(**{"Authorization": "Token $token"})
            .with_json(
                {
                    "goodsname": "$goodsname",
                    "goodscode": "$goodscode",
                    "merchantid": "$merchantid",
                    "merchantname": "$merchantname",
                    "goodsprice": "$goodsprice",
                    "stock": "$stock",
                    "goodsgroupid": "$goodsgroupid",
                    "goodsstatus": "$goodsstatus",
                    "price": "$price",
                }
            )
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCasePutGoodsGoodsprice().test_start()
