#!/bin/bash
(cd ..
./ckrew.sh ./testcase/mr-ckr-example-d/global.n3 ./testcase/mr-ckr-example-d/m_world19.n3 ./testcase/mr-ckr-example-d/m_branch19.n3 ./testcase/mr-ckr-example-d/m_branch20.n3 ./testcase/mr-ckr-example-d/m_local19.n3 -v -mrckr -out ./demo/output.dlv)
