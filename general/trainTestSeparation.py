'''
 * Copyright (C) 2017  Music Technology Group - Universitat Pompeu Fabra
 *
 * This file is part of jingjuSingingPhraseMatching
 *
 * pypYIN is free software: you can redistribute it and/or modify it under
 * the terms of the GNU Affero General Public License as published by the Free
 * Software Foundation (FSF), either version 3 of the License, or (at your
 * option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the Affero GNU General Public License
 * version 3 along with this program.  If not, see http://www.gnu.org/licenses/
 *
 * If you have any problem about this python version code, please contact: Rong Gong
 * rong.gong@upf.edu
 *
 *
 * If you want to refer this code, please use this article:
 *
'''

import os


def getRecordings(wav_path):
    """
    retrieve the filename from wav_path
    :param wav_path: not necessarily only contain .wav
    :return:
    """
    recordings      = []
    for root, subFolders, files in os.walk(wav_path):
            for f in files:
                file_prefix, file_extension = os.path.splitext(f)
                if file_prefix != '.DS_Store' and file_prefix != '_DS_Store':
                    recordings.append(file_prefix)

    return recordings

def getRecordingNames(train_test_string,mode):
    """
    reserved for other usage
    :param train_test_string:
    :param mode:
    :return:
    """
    if mode == 'laosheng':
        recordings_train = ['lseh-Tan_Yang_jia-Hong_yang_dong-qm', 'lseh-Wei_guo_jia-Hong_yang_dong01-lon', 'lseh-Wei_guo_jia-Hong_yang_dong02-qm', 'lseh-Yi_lun_ming-Wen_zhao_guan-qm', 'lseh-Zi_na_ri-Hong_yang_dong-qm', 'lsfxp-Yang_si_lang-Si_lang_tan_mu-lon', 'lsxp-Huai_nan_wang-Huai_he_ying01-lon', 'lsxp-Jiang_shen_er-San_jia_dian02-qm', 'lsxp-Qian_bai_wan-Si_lang_tang_mu01-qm', 'lsxp-Quan_qian_sui-Gan_lu_si-qm', 'lsxp-Shen_gong_wu-Gan_lu_si-qm', 'lsxp-Shi_ye_shuo-Ding_jun_shan-qm', 'lsxp-Wo_ben_shi-Kong_cheng_ji-qm', 'lsxp-Wo_zheng_zai-Kong_cheng_ji01-upf', 'lsxp-Wo_zheng_zai-Kong_cheng_ji04-qm', 'lsxp-Xi_ri_you-Zhu_lian_zhai-qm']
        recordings_test  = ['lseh-Wo_ben_shi-Qiong_lin_yan-qm', 'lsxp-Guo_liao_yi-Wen_zhao_guan-qm', 'lsxp-Guo_liao_yi-Wen_zhao_guan-upf', 'lsxp-Huai_nan_wang-Huai_he_ying02-qm', 'lsxp-Jiang_shen_er-San_jia_dian01-1-upf', 'lsxp-Jiang_shen_er-San_jia_dian01-2-upf', 'lsxp-Wo_zheng_zai-Kong_cheng_ji02-qm']
    elif mode == 'dan':
        recordings_train = ['shiwenhui_tingxiongyan', 'wangjiangting_zhijianta', 'xixiangji_diyilai', 'xixiangji_luanchouduo', 'xixiangji_manmufeng', 'xixiangji_zhenmeijiu', 'yutangchun_yutangchun', 'zhuangyuanmei_daocishi', 'zhuangyuanmei_tianbofu', 'zhuangyuanmei_zhenzhushan', 'zhuangyuanmei_zinari']
        recordings_test  = ['wangjiangting_dushoukong', 'xixiangji_biyuntian', 'xixiangji_xianzhishuo', 'zhuangyuanmei_fudingkui']


    if train_test_string == 'TRAIN':
        name_recordings      = recordings_train
    else:
        name_recordings      = recordings_test
    return name_recordings

def getRecordingNamesSimi(train_test,mode):
    '''
    return recordings names, test recordings in score dataset
    :param mode: role type
    :return:
    '''
    if mode == 'laosheng':
        recordings_train = ['lseh-Tan_Yang_jia-Hong_yang_dong-qm',
                            'lsfxp-Yang_si_lang-Si_lang_tan_mu-lon',
                            'lsxp-Qian_bai_wan-Si_lang_tang_mu01-qm',
                            'lsxp-Quan_qian_sui-Gan_lu_si-qm',
                            'lsxp-Shi_ye_shuo-Ding_jun_shan-qm',
                            'lsxp-Wo_zheng_zai-Kong_cheng_ji01-upf',
                            'lsxp-Wo_zheng_zai-Kong_cheng_ji04-qm',
                            'lsxp-Xi_ri_you-Zhu_lian_zhai-qm',
                            'lseh-Wo_ben_shi-Qiong_lin_yan-qm',
                            'lsxp-Guo_liao_yi-Wen_zhao_guan-qm',
                            'lsxp-Guo_liao_yi-Wen_zhao_guan-upf',
                            'lsxp-Huai_nan_wang-Huai_he_ying01-lon',
                            'lsxp-Wo_zheng_zai-Kong_cheng_ji02-qm']

        # these arias are in the score corpus 88 lines
        recordings_test = [
                      'lseh-Wei_guo_jia-Hong_yang_dong01-lon',
                      'lseh-Wei_guo_jia-Hong_yang_dong02-qm',
                      'lseh-Yi_lun_ming-Wen_zhao_guan-qm',
                      'lseh-Zi_na_ri-Hong_yang_dong-qm', # 4,5 not in corpus
                      'lsxp-Huai_nan_wang-Huai_he_ying02-qm', # 0,1,2,3 not in corpus
                      'lsxp-Jiang_shen_er-San_jia_dian01-1-upf',
                      'lsxp-Jiang_shen_er-San_jia_dian01-2-upf',
                      'lsxp-Jiang_shen_er-San_jia_dian02-qm',
                      'lsxp-Shen_gong_wu-Gan_lu_si-qm',
                      'lsxp-Wo_ben_shi-Kong_cheng_ji-qm']
    elif mode == 'danAll':

        recordings_train = ['daspd-Du_shou_kong-Wang_jiang_ting-upf',
                            'daeh-Bie_yuan_zhong-Mei_fei-qm',
                            'daeh-Yang_Yu_huan-Tai_zhen_wai_zhuan-lon',
                            'daeh-Yi_sha_shi-Suo_lin_nang-qm',
                            'daeh-You_He_hou-He_hou_ma_dian-qm',
                            'dafeh-Bi_yun_tian-Xi_xiang_ji01-qm',
                            'dafeh-Mo_lai_you-Liu_yue_xue-qm',
                            'dagbz-Feng_xiao_xiao-Yang_men_nv_jiang-lon',
                            'danbz-Bei_jiu_chan-Chun_gui_men03-qm',
                            'danbz-Kan_dai_wang-Ba_wang_bie_ji03-qm',
                            'danbz-Qing_chen_qi-Shi_yu_zhuo-qm',
                            'daspd-Hai_dao_bing-Gui_fei_zui_jiu01-lon',
                            'daxp-Jiao_Zhang_sheng-Hong_niang04-qm',
                            'daxp-Jiao_Zhang_sheng-Hong_niang05-qm',
                            'daxp-Chun_qiu_ting-Suo_lin_nang03-qm',
                            'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai02-qm',
                            'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai04-qm',
                            'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai06-qm',
                            'shiwenhui_tingxiongyan',
                            'xixiangji_biyuntian',
                            'xixiangji_diyilai',
                            'xixiangji_luanchouduo',
                            'xixiangji_manmufeng',
                            'xixiangji_xianzhishuo',
                            'xixiangji_zhenmeijiu',
                            'yutangchun_yutangchun',
                            'zhuangyuanmei_daocishi',
                            'zhuangyuanmei_fudingkui',
                            'zhuangyuanmei_tianbofu',
                            'zhuangyuanmei_zhenzhushan']

        # 72 lines (estimated) in score corpus

        recordings_test = ['zhuangyuanmei_zinari',
                           'daxp-Chun_qiu_ting-Suo_lin_nang01-qm',
                           'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai01-upf',
                           'daxp-Guan_Shi_yin-Tian_nv_san_hua-lon',
                           'danbz-Bei_jiu_chan-Chun_gui_men01-qm',
                           'danbz-Kan_dai_wang-Ba_wang_bie_ji01-qm',
                           'daspd-Hai_dao_bing-Gui_fei_zui_jiu02-qm',
                           'daxp-Jiao_Zhang_sheng-Hong_niang01-qm',
                           'daxp-Zhe_cai_shi-Suo_lin_nang01-qm',
                           'daxp-Xi_ri_li-Gan_lu_si-qm',
                           'wangjiangting_zhijianta',
                           'wangjiangting_dushoukong'
                           ]

    if train_test == 'TRAIN':
        return recordings_train
    else:
        return recordings_test


def getTestTrainRecordingsJoint():
    # train test recording for syllable and phoneme joint estimation
    # primary train and test set are not included
    trainNacta2017 = [['20170327LiaoJiaNi', 'lseh-Niang_zi_bu-Sou_gu_jiu-nacta'],  # yes
                      ['20170327LiaoJiaNi', 'lsxp-Yi_ma_li-Wu_jia_po-nacta'],
                      ['20170418TianHao', 'lseh-Tan_yang_jia-Hong_yang_dong-nacta']]  # yes

    trainNacta = [['danAll', 'dafeh-Bi_yun_tian-Xi_xiang_ji01-qm'],
                  ['danAll', 'danbz-Bei_jiu_chan-Chun_gui_men01-qm'],
                  ['danAll', 'danbz-Kan_dai_wang-Ba_wang_bie_ji01-qm'],
                  ['danAll', 'daspd-Hai_dao_bing-Gui_fei_zui_jiu02-qm'],
                  ['danAll', 'daxp-Chun_qiu_ting-Suo_lin_nang01-qm'],
                  ['danAll', 'daxp-Jiao_Zhang_sheng-Hong_niang01-qm'],
                  ['danAll', 'daxp-Meng_ting_de-Mu_Gui_ying_gua_shuai04-qm'],
                  ['danAll', 'daxp-Zhe_cai_shi-Suo_lin_nang01-qm'],
                  ['laosheng', 'lseh-Tan_Yang_jia-Hong_yang_dong-qm'],
                  ['laosheng', 'lseh-Wo_ben_shi-Qiong_lin_yan-qm'],
                  ['laosheng', 'lseh-Yi_lun_ming-Wen_zhao_guan-qm'],
                  ['laosheng', 'lseh-Zi_na_ri-Hong_yang_dong-qm'],
                  ['laosheng', 'lsxp-Guo_liao_yi-Wen_zhao_guan02-qm'],
                  ['laosheng', 'lsxp-Huai_nan_wang-Huai_he_ying02-qm'],
                  ['laosheng', 'lsxp-Jiang_shen_er-San_jia_dian02-qm'],
                  ['laosheng', 'lsxp-Qian_bai_wan-Si_lang_tang_mu01-qm'],
                  ['laosheng', 'lsxp-Quan_qian_sui-Gan_lu_si-qm'],
                  ['laosheng', 'lsxp-Shi_ye_shuo-Ding_jun_shan-qm'],
                  ['laosheng', 'lsxp-Wo_ben_shi-Kong_cheng_ji-qm'],
                  ['laosheng', 'lsxp-Xi_ri_you-Zhu_lian_zhai-qm'],
                  ['danAll', 'dagbz-Feng_xiao_xiao-Yang_men_nv_jiang-lon'],  # no
                  ['danAll', 'daspd-Du_shou_kong-Wang_jiang_ting-upf'],  # yes
                  ['danAll', 'daxp-Guan_Shi_yin-Tian_nv_san_hua-lon'],  # yes
                  ['laosheng', 'lsxp-Guo_liao_yi-Wen_zhao_guan01-upf']]

    testPrimarySchool = [['20171211SongRuoXuan/daxp_Qing_zao_qi_lai-Mai_shui-dxjky', 'student01']]

    return testPrimarySchool, trainNacta2017, trainNacta


