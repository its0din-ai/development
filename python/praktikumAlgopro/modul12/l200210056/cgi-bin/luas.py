#!/usr/bin/env python3

def luas(alas, tinggi):
    luas = alas * tinggi
    return luas

alas = 128
tinggi = 512

markup = f"""
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Kegiatan 3</title>
</head>
<body style="font-family: 'Open Sans', sans-serif !important; font-weight: 700; background-color: #e8e8e4">

    <div class="container container-fluid ms-5 mt-5">
        <div class="card mb-3" style="max-width: 800px; background-color: #d8e2dc;">
            <div class="row g-0">
              <div class="col-md-8">
                <div class="card-body">
                  <h3 class="card-title"><strong>BANGUN GEOMETRI</strong></h3>
                  <p class="card-text">
                    <table class="table table-borderless table-sm">
                        <tbody>
                          <tr>
                            <th scope="row" width="100px">NAMA BANGUN</th>
                            <td width="2px">:</td>
                            <td width="220px">JAJAR GENJANG</td>
                          </tr>
                          <tr>
                            <th scope="row">DIMENSI</th>
                            <td>:</td>
                            <td>2 DIMENSI</td>
                          </tr>
                          <tr>
                            <th scope="row">RUMUS LUAS</th>
                            <td>:</td>
                            <td>ALAS &#215; TINGGI</td>
                          </tr>
                          <tr>
                            <th scope="row">ALAS</th>
                            <td>:</td>
                            <td>{alas} CM</td>
                          </tr>
                          <tr>
                            <th scope="row">TINGGI</th>
                            <td>:</td>
                            <td>{tinggi} CM</td>
                          </tr>
                          <tr>
                            <th scope="row">LUAS</th>
                            <td>:</td>
                            <td>{luas(alas, tinggi):,} CM<sup>2</sup></td>
                          </tr>
                        </tbody>
                      </table>
                  </p>
                </div>
              </div>
            </div>
        </div>
    </div>
</body>"""

print(markup)