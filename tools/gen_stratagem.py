import json
from ast import Dict
from hashlib import md5
from pathlib import Path
from typing import List

import requests

from src.model import Stratagem


def g(*args, **kwargs) -> dict:
    return Stratagem.gen_by_short_code(*args, **kwargs).model_dump()


STRATAGEM_LIST: List[dict] = [
    g(
        name="Reinforce",
        name_zh="增援",
        short_name_zh="增援",
        short_code="wsdaw",
        icon="https://helldivers.wiki.gg/images/5/5c/Reinforce_Stratagem_Icon.png",
    ),
    g(
        name="SoS Beacon",
        name_zh="S.O.S求援信标",
        short_name_zh="S.O.S求援信标",
        short_code="wsdw",
        icon="https://helldivers.wiki.gg/images/3/3d/SOS_Beacon_Stratagem_Icon.png",
    ),
    g(
        name="Hellbomb",
        name_zh="地狱火炸弹",
        short_name_zh="地狱火炸弹",
        short_code="swaswdsw",
        icon="https://helldivers.wiki.gg/images/a/a0/Hellbomb_Stratagem_Icon.png",
    ),
    g(
        name="MG-43 Machine Gun",
        name_zh="MG-43 机枪",
        short_name_zh="机枪",
        short_code="saswd",
        icon="https://helldivers.wiki.gg/images/e/e0/Machine_Gun_Stratagem_Icon.png",
    ),
    g(
        name="APW-1 Anti-Materiel Rifle",
        name_zh="APW-1 反器材步枪",
        short_name_zh="反器材步枪",
        short_code="sadws",
        icon="https://helldivers.wiki.gg/images/3/3c/Anti-Materiel_Rifle_Stratagem_Icon.png",
    ),
    g(
        name="M-105 Stalwart",
        name_zh="M-105 盟友",
        short_name_zh="盟友",
        short_code="saswwa",
        icon="https://helldivers.wiki.gg/images/4/46/Stalwart_Stratagem_Icon.png",
    ),
    g(
        name="EAT-17 Expendable Anti-Tank",
        name_zh="EAT-17 消耗性反坦克武器",
        short_name_zh="消耗性反坦克武器",
        short_code="ssawd",
        icon="https://helldivers.wiki.gg/images/1/1c/Expendable_Anti-Tank_Stratagem_Icon.png",
    ),
    g(
        name="GR-8 Recoilless Rifle",
        name_zh="GR-8 无后座力步枪",
        short_name_zh="无后座力步枪",
        short_code="sadda",
        icon="https://helldivers.wiki.gg/images/7/70/Recoilless_Rifle_Stratagem_Icon.png",
    ),
    g(
        name="FLAM-40 Flamethrower",
        name_zh="FLAM-40 火焰喷射器",
        short_name_zh="火焰喷射器",
        short_code="sawsw",
        icon="https://helldivers.wiki.gg/images/7/75/Flamethrower_Stratagem_Icon.png",
    ),
    g(
        name="AC-8 Autocannon",
        name_zh="AC-8 机炮",
        short_name_zh="机炮",
        short_code="saswwd",
        icon="https://helldivers.wiki.gg/images/e/ef/Autocannon_Stratagem_Icon.png",
    ),
    g(
        name="MG-206 Heavy Machine Gun",
        name_zh="MG-206 重机枪",
        short_name_zh="重机枪",
        short_code="sawss",
        icon="https://helldivers.wiki.gg/images/d/d9/Heavy_Machine_Gun_Stratagem_Icon.png",
    ),
    g(
        name="RS-422 Railgun",
        name_zh="RS-422 磁轨炮",
        short_name_zh="磁轨炮",
        short_code="sdswad",
        icon="https://helldivers.wiki.gg/images/3/35/Railgun_Stratagem_Icon.png",
    ),
    g(
        name="FAF-14 Spear",
        name_zh="FAF-14 飞矛",
        short_name_zh="飞矛",
        short_code="sswss",
        icon="https://helldivers.wiki.gg/images/5/54/Spear_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Gatling Barrage",
        name_zh="轨道加特林火力网",
        short_name_zh="轨道加特林火力网",
        short_code="dsaww",
        icon="https://helldivers.wiki.gg/images/f/f6/Orbital_Gatling_Barrage_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Airburst Strike",
        name_zh="轨道空爆攻击",
        short_name_zh="轨道空爆攻击",
        short_code="ddd",
        icon="https://helldivers.wiki.gg/images/2/28/Orbital_Airburst_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Orbital 120mm HE Barrage",
        name_zh="轨道120MM高爆弹火力网",
        short_name_zh="轨道120MM高爆弹火力网",
        short_code="dssasdss",
        icon="https://helldivers.wiki.gg/images/4/40/Orbital_120mm_HE_Barrage_Stratagem_Icon.png",
    ),
    g(
        name="Orbital 380mm HE Barrage",
        name_zh="轨道380MM高爆弹火力网",
        short_name_zh="轨道380MM高爆弹火力网",
        short_code="dswwass",
        icon="https://helldivers.wiki.gg/images/1/12/Orbital_380mm_HE_Barrage_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Walking Barrage",
        name_zh="轨道游走火力网",
        short_name_zh="轨道游走火力网",
        short_code="dsdsds",
        icon="https://helldivers.wiki.gg/images/5/53/Orbital_Walking_Barrage_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Laser",
        name_zh="轨道激光炮",
        short_name_zh="轨道激光炮",
        short_code="dswds",
        icon="https://helldivers.wiki.gg/images/d/d8/Orbital_Laser_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Railcannon Strike",
        name_zh="轨道炮攻击",
        short_name_zh="轨道炮攻击",
        short_code="dwssd",
        icon="https://helldivers.wiki.gg/images/6/6f/Orbital_Railcannon_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Eagle Strafing Run",
        name_zh='"飞鹰"机枪扫射',
        short_name_zh='"飞鹰"机枪扫射',
        short_code="wdd",
        icon="https://helldivers.wiki.gg/images/f/f3/Eagle_Strafing_Run_Stratagem_Icon.png",
    ),
    g(
        name="Eagle Airstrike",
        name_zh='"飞鹰"空袭',
        short_name_zh='"飞鹰"空袭',
        short_code="wdsd",
        icon="https://helldivers.wiki.gg/images/7/72/Eagle_Airstrike_Stratagem_Icon.png",
    ),
    g(
        name="Eagle Cluster Bomb",
        name_zh='"飞鹰"集束炸弹',
        short_name_zh='"飞鹰"集束炸弹',
        short_code="wdssd",
        icon="https://helldivers.wiki.gg/images/4/4f/Eagle_Cluster_Bomb_Stratagem_Icon.png",
    ),
    g(
        name="Eagle Napalm Airstrike",
        name_zh='"飞鹰"凝固汽油弹空袭',
        short_name_zh='"飞鹰"凝固汽油弹空袭',
        short_code="wdsw",
        icon="https://helldivers.wiki.gg/images/4/42/Eagle_Napalm_Airstrike_Stratagem_Icon.png",
    ),
    g(
        name="Lift-850 Jump Pack",
        name_zh="喷射背包",
        short_name_zh="喷射背包",
        short_code="swwsw",
        icon="https://helldivers.wiki.gg/images/f/f5/Jump_Pack_Stratagem_Icon.png",
    ),
    g(
        name="Eagle Smoke Strike",
        name_zh='"飞鹰"烟雾攻击',
        short_name_zh='"飞鹰"烟雾攻击',
        short_code="wdws",
        icon="https://helldivers.wiki.gg/images/0/05/Eagle_Smoke_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Eagle 110mm Rocket Pods",
        name_zh='"飞鹰"110MM火箭巢',
        short_name_zh='"飞鹰"110MM火箭巢',
        short_code="wdwa",
        icon="https://helldivers.wiki.gg/images/e/ef/Eagle_110mm_Rocket_Pods_Stratagem_Icon.png",
    ),
    g(
        name="Eagle 500kg Bomb",
        name_zh='"飞鹰"500KG炸弹',
        short_name_zh='"飞鹰"500KG炸弹',
        short_code="wdsss",
        icon="https://helldivers.wiki.gg/images/e/e5/Eagle_500kg_Bomb_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Precision Strike",
        name_zh="轨道精准攻击",
        short_name_zh="轨道精准攻击",
        short_code="ddw",
        icon="https://helldivers.wiki.gg/images/2/2a/Orbital_Precision_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Gas Strike",
        name_zh="轨道毒气攻击",
        short_name_zh="轨道毒气攻击",
        short_code="ddsd",
        icon="https://helldivers.wiki.gg/images/c/cd/Orbital_Gas_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Orbital EMS Strike",
        name_zh="轨道电磁冲击波攻击",
        short_name_zh="轨道电磁冲击波攻击",
        short_code="ddas",
        icon="https://helldivers.wiki.gg/images/1/16/Orbital_EMS_Strike_Stratagem_Icon.png",
    ),
    g(
        name="Orbital Smoke Strike",
        name_zh="轨道烟雾攻击",
        short_name_zh="轨道烟雾攻击",
        short_code="ddsw",
        icon="https://helldivers.wiki.gg/images/b/bc/Orbital_Smoke_Strike_Stratagem_Icon.png",
    ),
    g(
        name="E/MG-101 HMG Emplacement",
        name_zh="重机枪部署支架",
        short_name_zh="重机枪部署支架",
        short_code="swadda",
        icon="https://helldivers.wiki.gg/images/0/03/HMG_Emplacement_Stratagem_Icon.png",
    ),
    g(
        name="FX-12 Shield Generator Relay",
        name_zh="防护罩生成中继器",
        short_name_zh="防护罩生成中继器",
        short_code="ssadad",
        icon="https://helldivers.wiki.gg/images/e/e4/Shield_Generator_Relay_Stratagem_Icon.png",
    ),
    g(
        name="A/ARC-3 Tesla Tower",
        name_zh="特斯拉塔",
        short_name_zh="特斯拉塔",
        short_code="swdwad",
        icon="https://helldivers.wiki.gg/images/8/8f/Tesla_Tower_Stratagem_Icon.png",
    ),
    g(
        name="MD-6 Anti-Personnel Minefield",
        name_zh="反步兵雷区",
        short_name_zh="反步兵雷区",
        short_code="sawd",
        icon="https://helldivers.wiki.gg/images/b/bb/Anti-Personnel_Minefield_Stratagem_Icon.png",
    ),
    g(
        name="B-1 Supply Pack",
        name_zh="补给背包",
        short_name_zh="补给背包",
        short_code="saswwd",
        icon="https://helldivers.wiki.gg/images/6/61/Supply_Pack_Stratagem_Icon.png",
    ),
    g(
        name="GL-21 Grenade Launcher",
        name_zh="榴弹发射器",
        short_name_zh="榴弹发射器",
        short_code="sawas",
        icon="https://helldivers.wiki.gg/images/c/cf/Grenade_Launcher_Stratagem_Icon.png",
    ),
    g(
        name="LAS-98 Laser Cannon",
        name_zh="激光大炮",
        short_name_zh="激光大炮",
        short_code="saswa",
        icon="https://helldivers.wiki.gg/images/c/c3/Laser_Cannon_Stratagem_Icon.png",
    ),
    g(
        name="MD-I4 Incendiary Mines",
        name_zh="燃烧地雷",
        short_name_zh="燃烧地雷",
        short_code="saas",
        icon="https://helldivers.wiki.gg/images/a/a9/Incendiary_Minefield_Stratagem_Icon.png",
    ),
    g(
        name='AX/LAS-5 "Guard Dog" Rover',
        name_zh='"护卫犬"漫游车',
        short_name_zh='"护卫犬"漫游车',
        short_code="swawdd",
        icon="https://helldivers.wiki.gg/images/6/6f/Guard_Dog_Rover_Stratagem_Icon.png",
    ),
    g(
        name="SH-20 Ballistic Shield Backpack",
        name_zh="防弹护盾背包",
        short_name_zh="防弹护盾背包",
        short_code="sasswa",
        icon="https://helldivers.wiki.gg/images/3/37/Ballistic_Shield_Backpack_Stratagem_Icon.png",
    ),
    g(
        name="ARC-3 Arc Thrower",
        name_zh="电弧发射器",
        short_name_zh="电弧发射器",
        short_code="sdswaa",
        icon="https://helldivers.wiki.gg/images/1/10/Arc_Thrower_Stratagem_Icon.png",
    ),
    g(
        name="LAS-99 Quasar Cannon",
        name_zh="类星体加农炮",
        short_name_zh="类星体加农炮",
        short_code="sswad",
        icon="https://helldivers.wiki.gg/images/8/87/Quasar_Cannon_Stratagem_Icon.png",
    ),
    g(
        name="SH-32 Shield Generator Pack",
        name_zh="防护罩生成包",
        short_name_zh="防护罩生成包",
        short_code="swadad",
        icon="https://helldivers.wiki.gg/images/9/99/Shield_Generator_Pack_Stratagem_Icon.png",
    ),
    g(
        name="A/MG-43 Machine Gun Sentry",
        name_zh="哨戒机枪",
        short_name_zh="哨戒机枪",
        short_code="swddw",
        icon="https://helldivers.wiki.gg/images/5/5a/Machine_Gun_Sentry_Stratagem_Icon.png",
    ),
    g(
        name="A/G-16 Gatling Sentry",
        name_zh="加特林哨戒炮",
        short_name_zh="加特林哨戒炮",
        short_code="swda",
        icon="https://helldivers.wiki.gg/images/2/28/Gatling_Sentry_Stratagem_Icon.png",
    ),
    g(
        name="A/M-12 Mortar Sentry",
        name_zh="迫击哨戒炮",
        short_name_zh="迫击哨戒炮",
        short_code="swdds",
        icon="https://helldivers.wiki.gg/images/a/ad/Mortar_Sentry_Stratagem_Icon.png",
    ),
    g(
        name='AX/AR-23 "Guard Dog"',
        name_zh='"护卫犬"',
        short_name_zh='"护卫犬"',
        short_code="swawds",
        icon="https://helldivers.wiki.gg/images/7/73/Guard_Dog_Stratagem_Icon.png",
    ),
    g(
        name="A/AC-8 Autocannon Sentry",
        name_zh="自动哨戒炮",
        short_name_zh="自动哨戒炮",
        short_code="swdwaw",
        icon="https://helldivers.wiki.gg/images/a/a7/Autocannon_Sentry_Stratagem_Icon.png",
    ),
    g(
        name="A/MLS-4X Rocket Sentry",
        name_zh="火箭哨戒炮",
        short_name_zh="火箭哨戒炮",
        short_code="swdda",
        icon="https://helldivers.wiki.gg/images/6/62/Rocket_Sentry_Stratagem_Icon.png",
    ),
    g(
        name="A/M-23 EMS Mortar Sentry",
        name_zh="电磁冲击波迫击哨戒炮",
        short_name_zh="电磁冲击波迫击哨戒炮",
        short_code="swdsd",
        icon="https://helldivers.wiki.gg/images/a/a8/AM-23_EMS_Mortar_Sentry_Stratagem_Icon.png",
    ),
    g(
        name="EXO-45 Patriot Exosuit",
        name_zh='"爱国者"外骨骼装甲',
        short_name_zh='"爱国者"外骨骼装甲',
        short_code="asdwass",
        icon="https://helldivers.wiki.gg/images/3/30/EXO-45_Patriot_Exosuit_Stratagem_Icon.png",
    ),
]


def main():
    Path("data").mkdir(parents=True, exist_ok=True)
    Path("static/icon").mkdir(parents=True, exist_ok=True)

    for stratagem in STRATAGEM_LIST:
        # 将所有的图标下载到本地
        if not stratagem["icon"]:
            continue
        suffix = stratagem["icon"].split(".")[-1]
        md5_url = str(md5(stratagem["icon"].encode("utf-8")).hexdigest())
        icon = stratagem["icon"]
        if not Path(f"./static/icon/{md5_url}.{suffix}").exists():
            print(f"downloading {icon}")
            url = f"{icon}"
            r = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
                },
                proxies={
                    "http": "http://127.0.0.1:7890",
                    "https": "http://127.0.0.1:7890",
                },
                timeout=10,
                verify=False,
            )
            with open(f"./static/icon/{md5_url}.{suffix}", "wb") as f:  # noqa: PTH123
                f.write(r.content)
    with open("./static/stratagem.json", "w", encoding="utf-8") as f:  # noqa: PTH123
        f.write(json.dumps(STRATAGEM_LIST, ensure_ascii=False, indent=4))
