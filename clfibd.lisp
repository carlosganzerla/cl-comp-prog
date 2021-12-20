(defconstant +dynamic+ "Dynamic")
(defconstant +not+ "Not")


(defun check-dynamic (permutations)
  )

(defun get-permutations (table)
  (let ((idx 0)
        (set (make-hash-table :size 26 :element-type 'fixnum)))
    (maphash (lambda (k v) 
               (cond ((not (gethash v set)) (setf (gethash v set) v))
                     ((not (gethash (/ 1 v) set)) (setf (gethash v set) v))))
            table)
    (sort (make-array (hash-table-count set)) #'>)))

(defun get-chars (str)
  (let ((table (make-hash-table :size 26)))
    (dotimes (i (length str) (check-dynamic table))
      (if (not (gethash (char str i) table))
          (setf (gethash (char str i) table) 1)
          (incf (gethash (char str i) table))))))

(defun get-chars2 (str)
  (let ((table (make-array 26 :element-type 'fixnum)))
    (dotimes (i (length str))
      ()
      )
    )
  )

(dotimes (x (read))
  (print (get-dynamic (read))))

