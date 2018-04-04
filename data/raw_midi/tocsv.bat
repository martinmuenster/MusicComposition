for %%f in (*.mid) do (
    echo %%~nf
    midicsv "%%~nf.mid" "%%~nf.csv"
)