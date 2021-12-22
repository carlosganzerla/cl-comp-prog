(defun sum (vec)
  (do ((i 0 (1+ i))
       (sum 0))
      ((>= i (length vec)) sum)
      (incf sum (aref vec i))))

(defun get-ans (vec k)
  (do ((i 0 (1+ i))
       (sum 0))
      ((or (>= i (length vec)) (> (aref vec i)
                                  (aref vec (1- k))))

       (subseq vec 0 i))))

(get-ans #(1 1 2 2 2 2 3 3 3 4) 3)


(defun get-interesting (vec sum k n)
  (do ((i 0 (1+ i))
       (total 0))
      ((>= i (- n k)))
      (do ((j (+ k i) (1+ j))
           (current sum (+ sum (- (aref vec j) (aref vec (1- j))))))
          ((>= j n))
          (when (= current sum)
            (incf total)))))
