import requests
import json

def denovo_sequence(mz, charge, peaks, urlbase="mingwangbeta.ucsd.edu"):
    url = "http://%s:5100/kaikodeepnovo" % (urlbase)

    payload = {'precursormz': mz, 'charge': charge, "peaks": json.dumps(peaks)}
    r = requests.get(url, params=payload)

    return r.json()

def test_api1():
    mz = "478.2704070130128"
    charge = 4
    peaks = json.loads('[["119.02627563476562", "392.2457275390625"], ["129.1024169921875", "12147.2705078125"], ["130.1060028076172", "666.388916015625"], ["136.06167602539062", "823.4880981445312"], ["145.09689331054688", "972.2864990234375"], ["156.7694854736328", "361.78607177734375"], ["164.85572814941406", "417.0838317871094"], ["170.10325622558594", "456.71221923828125"], ["173.0915069580078", "444.4327697753906"], ["175.1190643310547", "6938.96533203125"], ["186.12355041503906", "2749.39990234375"], ["192.22216796875", "362.2316589355469"], ["283.1388244628906", "3266.9853515625"], ["354.1733093261719", "705.064453125"], ["397.3297119140625", "421.1595458984375"], ["437.5796203613281", "2514.0849609375"], ["437.91693115234375", "1735.205078125"], ["438.2517395019531", "406.9606018066406"], ["448.7451171875", "445.42236328125"], ["455.2225646972656", "577.8519897460938"], ["458.7539367675781", "402.63006591796875"], ["474.01434326171875", "934.3148803710938"], ["474.27203369140625", "581.1235961914062"], ["495.8350830078125", "4186.46337890625"], ["531.6235961914062", "817.3599243164062"], ["548.3114624023438", "485.83160400390625"], ["556.8167114257812", "1748.2828369140625"], ["557.3126220703125", "535.7135009765625"], ["568.8131103515625", "724.7904052734375"], ["569.3073120117188", "587.5978393554688"], ["577.3114013671875", "487.2419738769531"], ["577.81494140625", "2499.495361328125"], ["578.3125", "494.83868408203125"], ["584.3173828125", "487.23291015625"], ["595.3419189453125", "582.517578125"], ["598.8284301757812", "702.2935791015625"], ["599.3284301757812", "681.7647094726562"], ["600.344970703125", "558.9706420898438"], ["604.349853515625", "571.6264038085938"], ["607.34326171875", "3133.679443359375"], ["607.8345947265625", "740.2290649414062"], ["612.3402099609375", "611.374267578125"], ["624.8550415039062", "613.9937744140625"], ["625.8565063476562", "2905.38330078125"], ["626.3489990234375", "2306.8974609375"], ["626.8512573242188", "933.8587646484375"], ["633.8519287109375", "2563.092041015625"], ["634.3541870117188", "1895.78076171875"], ["646.8584594726562", "2862.70263671875"], ["647.357177734375", "4704.8896484375"], ["647.8567504882812", "2356.06591796875"], ["655.868408203125", "7795.02734375"], ["656.3654174804688", "2066.872802734375"], ["656.8717041015625", "536.8590698242188"], ["739.9118041992188", "464.8411560058594"], ["748.4151611328125", "488.1359558105469"], ["748.9214477539062", "565.3721923828125"], ["1094.58740234375", "663.1194458007812"], ["1136.600830078125", "1888.6258544921875"], ["1198.955078125", "485.7593688964844"]]')

    print(denovo_sequence(mz,charge,peaks))