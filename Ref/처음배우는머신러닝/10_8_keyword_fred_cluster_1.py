import time
from scipy import stats
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random
import numpy as np
from sklearn.metrics import silhouette_score

# 데이터 구조 정의
# 사용자 ID를 키로, 상품 코드의 셋을 밸류로 갖는 딕셔너리와
# 상품 코드를 키로, 사용자 ID의 셋을 밸류로 갖는 딕셔너리
user_product_dic = {}
product_user_dic = {}

# 상품 코드를 키로 가지고 상품명을 밸류로 갖는 딕셔너리
# 군집화의 내용을 확인하는 단계에서 상품명을 사용합니다.
product_id_name_dic = {}


def analyze_clusters_keywords(labels, product_id_name_dic, user_product_dic, id_user_dic):
    # 각 클러스터의 아이디와, 해당 아이디의 클러스터 들어있는 유저 수를 출력합니다.
    print(Counter(labels))
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])

        # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
        # 그 사용자 코드와 연결된 구매상품의 ID를 참조한 후
        # 그 ID를 이용해 상품명을 찾아
        # 딕셔너리에 클러스터 ID를 키로, 상품명을 값으로 추가합니다.
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        # 각 클러스터안의 상품명을 join명령으로 합쳐 하나의 문자열로 만든 뒤
        # 스페이스 혹은 탭으로 스플릿하여 키워드로 분해합니다.
        product_name_keyword = (" ").join(product_name).split()

        # 클러스터의 아이디와, 그 아이디를 가지는 클러스터에 속하는 유저들이 구매한 상품들의 상품명안에
        # 가장 자주 나타나는 단어 20개를 역순으로 출력합니다
        print("cluster_id:", cluster_id)
        print(Counter(product_name_keyword).most_common(20))

# 파일을 읽어 위에 정의한 데이터구조를 채웁니다.
for line in open('online_retail_utf.txt'):

    # 데이터를 한 행씩 읽어서 필요한 항목을 저장합니다.
    line_items = line.strip().split('\t')
    user_code = line_items[6]
    product_id = line_items[1]
    product_name = line_items[2]

    # 사용자 ID가 없을 경우 무시합니다.
    if len(user_code) == 0:
        continue

    # 영국에서 구매한 사용자만 고려하므로, 국가가 united kingdom이 아닌 경우엔 무시합니다.
    country = line_items[7]
    if country != 'United Kingdom':
        continue

    # 연도 읽을 때 에러 처리. 파일 헤더를 무시합니다.
    try:
        invoice_year = time.strptime(line_items[4], '%m/%d/%y %H:%M').tm_year

    except ValueError:
        continue

    # 2011년에 일어난 구매가 아닌 것은 무시합니다.
    if invoice_year != 2011:
        continue

    # 읽은 정보로 데이터 구조를 채웁니다.
    # 상품 가짓수를 고려하므로 상품 코드를 셋으로 가지도록 하겠습니다.
    user_product_dic.setdefault(user_code, set())
    user_product_dic[user_code].add(product_id)

    product_user_dic.setdefault(product_id, set())
    product_user_dic[product_id].add(user_code)

    product_id_name_dic[product_id] = product_name

# 데이터구조를 다 채웠으므로 각 사용자들이 구매한 상품 가짓수로 리스트를 만들어봅시다.
product_per_user_li = [len(x) for x in user_product_dic.values()]


# 이 장에서 사용할 최종 사용자 수와 상품 가짓수를 출력해봅니다.
print('# of users:', len(user_product_dic))
print('# of products:', len(product_user_dic))

# 각 사용자들이 구매한 상품 가짓수로 기초 통계량을 출력합니다.
print(stats.describe(product_per_user_li))

# 사용자가 구매한 고유 상품 가짓수를 플롯해봅니다.
plot_data_all = Counter(product_per_user_li)
plot_data_x = list(plot_data_all.keys())
plot_data_y = list(plot_data_all.values())
plt.xlabel('고유 상품 가짓수')
plt.ylabel('사용자 수')
plt.scatter(plot_data_x, plot_data_y, marker='+')
plt.show()

# 구매한 상품의 가짓수가 1인 사용자의 사용자 ID를 찾습니다.
min_product_user_li =[k for k,v in user_product_dic.items() if len(v)==1]
# 마찬가지로, 구매한 상품의 가짓수가 600개 이상인 사용자의 사용자 ID를 찾습니다.
max_product_user_li =[k for k,v in user_product_dic.items() if len(v)>=600]
print("# of users purchased one product:%d" % (len(min_product_user_li)))
print("# of users purchased more than 600 product:%d" % (len(max_product_user_li)))
# 찾아낸 사용자를 군집화에 사용할 user_product_dic에서 제외합니다.
user_product_dic = {k:v for k,v in user_product_dic.items() if len(v)>1 and len(v)<600}
print("# of left user:%d" % (len(user_product_dic)))
# 남아 있는 사용자가 구매한 상품에도 0에서 시작하는 고유 ID를 부여합니다.
# 데이터셋에서 제외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에 이러한 처리를 해야 합니다.
id_product_dic = {}
for product_set_li in user_product_dic.values():
    for x in product_set_li:
        if x in id_product_dic:
            product_id = id_product_dic[x]
        else:
            id_product_dic.setdefault(x, len(id_product_dic))
print("# of left items:%d" % (len(id_product_dic)))

id_user_dic = {}

# 군집화의 입력으로 사용할 리스트
user_product_vec_li = []

# 군집화에서 사용할 총 고유 상품 가짓수. 즉, 원-핫 인코딩으로 변환할 피처의 가짓수
all_product_count = len(id_product_dic)

for user_code, product_per_user_set in user_product_dic.items():
    # 고유 상품 가짓수를 길이로 하는 리스트 생성
    user_product_vec = [0] * all_product_count
    # id_user_dic의 길이를 이용하여 사용자 ID를 0부터 시작하는 user_id로 바꿉니다.
    id_user_dic[len(id_user_dic)] = user_code

    # 사용자가 구매한 상품 코드를 키로 하여 user_product_vec에서의
    # 해당 상품 코드의 상품 ID를 찾습니다. 그리고 값을 1로 세팅합니다.
    for product_name in product_per_user_set:
        user_product_vec[id_product_dic[product_name]] = 1

    # 한 사용자의 처리가 끝났으므로 이 사용자의 user_product_vec을 배열에 추가합니다.
    # 이때 배열의 인덱스는 새로 정의한 user_id가 됩니다.
    user_product_vec_li.append(user_product_vec)

print(id_user_dic[0])
print(user_product_dic['17080'])
print(user_product_vec_li[0])
print(len(user_product_vec_li[0]))


print("\n<10_6>")
test_data = np.array(user_product_vec_li)

# for k in range(2,9):
#     km = KMeans(n_clusters=k).fit(test_data)
#     print("score for %d clusters:%.3f" % (k, silhouette_score(test_data,km.labels_)))

print("\n<10-8>")
km=KMeans(n_clusters=2, n_init=10,max_iter=20)
km.fit(test_data)
analyze_clusters_keywords(km.labels_,product_id_name_dic,user_product_dic,id_user_dic)